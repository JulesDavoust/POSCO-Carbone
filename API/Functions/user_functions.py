from flask import jsonify, request
from flask_mail import Message

import Models.models as models
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import jwt
import re
import logging


def signin(data, app):
    print(data)
    if not data or not data.get('email') or not data.get('password'):
        return {'message': 'Email and password are required!'}, 400

    user = models.Utilisateur_EFREI.query.filter_by(Email=data['email']).first()

    if not user:
        return {'message': 'User Not found.'}, 404

    if not check_password_hash(user.MotDePasse_Utilisateur, data['password']):
        return {'accessToken': None, 'message': 'Invalid Password!'}, 401

    token = jwt.encode({
        'userID': user.Num_Utilisateur,
        # 'isAdmin': user.isAdmin,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return {
        'userID': user.Num_Utilisateur,
        'email': user.Email,
        'accessToken': token
    }, 200


def register(data, db):
    promotion = [1, 2, 3, 4, 5]
    email_regex = r'^\S+@\S+\.\S+$'
    print("Data received: ", data)
    
    if not re.match(email_regex, data.get('emailUser', '')):
        print("Invalid email format")
        return {'message': 'Not valid format'}, 500

    if 'passwordUser' not in data:
        print("Password is required")
        return {'message': 'Password is required'}, 400
    
    if 'prenomUser' not in data:
        print("Prenom is required")
        return {'message': 'Prenom is required'}, 400
    
    if 'nomUser' not in data:
        print("Nom is required")
        return {'message': 'Nom is required'}, 400
    
    if 'numUser' not in data:
        print("Numéro étudiant is required")
        return {'message': 'Numéro étudiant is required'}, 400
    
    if 'promoUser' not in data:
        print("Promotion is required")
        return {'message': 'Promotion is required'}, 400

    idPromotion = 0
    if data['promoUser'] == 'L1':
        idPromotion = 1
    elif data['promoUser'] == 'L2':
        idPromotion = 2
    elif data['promoUser'] == 'L3':
        idPromotion = 3
    elif data['promoUser'] == 'M1':
        idPromotion = 4
    elif data['promoUser'] == 'M2':
        idPromotion = 5

    new_user = {
        'Email': data['emailUser'],
        'Prénom': data['prenomUser'],
        'Nom': data['nomUser'],
        'Num_Utilisateur': data['numUser'],
        'ID_Promotion': idPromotion,
        'MotDePasse_Utilisateur': generate_password_hash(data['passwordUser']),
        'notification_swim':None,
        'notification_semestre':None,
        'token_swim': None,
        'token_semestre': None
    }
    print('New user data: ', new_user)

    try:
        print("Checking if user already exists")
        existing_user = models.Utilisateur_EFREI.query.filter_by(Email=data['emailUser']).first()
        print("Existing user: ", existing_user)
        if existing_user:
            print("Email already taken")
            return {'message': 'Email already taken'}, 400

        print("Creating new user")
        user = models.Utilisateur_EFREI(**new_user)
        db.session.add(user)
        db.session.commit()
        print("User registered successfully")

        # Ajouter les entrées dans Répondre pour chaque question
        print("Adding default responses for the new user")
        questions = models.Question.query.all()
        for question in questions:
            new_reponse = models.Répondre(
                Num_Utilisateur=user.Num_Utilisateur,
                ID_Question=question.ID_Question,
                Faite=False
            )
            db.session.add(new_reponse)
        db.session.commit()
        print("User registered successfully with default responses")
        
        return {'message': 'Registered'}, 200
    except Exception as e:
        print("Error during registration: ", str(e))
        return {'message': str(e) or 'Some error occurred while creating the new user.'}, 500

def set_notification_swim(user_id, app, db):
    user = models.Utilisateur_EFREI.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    user.notification_swim = True
    db.session.commit()
    return jsonify({'message': 'Notification swim set to true'}), 200

def set_notification_semestre(user_id, app, db):
    user = models.Utilisateur_EFREI.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    user.notification_semestre = True
    db.session.commit()
    return jsonify({'message': 'Notification semestre set to true'}), 200

def send_notifications(app, db, mail):
    with app.app_context():
        users = db.session.query(models.Utilisateur_EFREI).filter(
            (models.Utilisateur_EFREI.notification_swim == True) |
            (models.Utilisateur_EFREI.notification_semestre == True)
        ).all()

        for user in users:
            try:
                expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
                if user.notification_swim:
                    payload = {
                        'user_id': user.Num_Utilisateur,
                        'exp': expiration,
                        'type': 'swim',
                        'completed': False
                    }
                    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
                    user.token_swim = token

                    link = f"http://localhost:8080/questionnaire_swim?token={token}"
                    msg = Message('Weekly SWIM Notification', sender=app.config['MAIL_USERNAME'], recipients=[user.Email])
                    msg.body = f'Please complete the weekly SWIM questionnaire by clicking on the following link: {link}'
                    mail.send(msg)

                if user.notification_semestre:
                    payload = {
                        'user_id': user.Num_Utilisateur,
                        'exp': expiration,
                        'type': 'semestre',
                        'completed': False
                    }
                    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
                    user.token_semestre = token

                    link = f"http://localhost:8080/questionnaire_sem?token={token}"
                    msg = Message('Semester Notification', sender=app.config['MAIL_USERNAME'], recipients=[user.Email])
                    msg.body = f'Please complete the semester questionnaire by clicking on the following link: {link}'
                    mail.send(msg)

                db.session.commit()
            except Exception as e:
                db.session.rollback()
                continue


def check_and_update_swim_notification(user_id, db):
    user = models.Utilisateur_EFREI.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Supposez que ID_Formulaire pour SWIM est une constante connue
    SWIM_FORMULAIRE_ID = 1  # Remplacez par l'ID correct du formulaire SWIM

    # Récupérer toutes les questions liées au formulaire SWIM
    questions = db.session.query(models.Question).join(models.Avoir).filter(
        models.Avoir.ID_Formulaire == SWIM_FORMULAIRE_ID
    ).all()

    # Vérifier si toutes les questions sont faites
    all_done = all(question.Faite for question in questions)

    if all_done:
        user.notification_swim = False
        db.session.commit()
        return jsonify({'message': 'All SWIM questions are done. notification_swim set to false'}), 200
    else:
        return jsonify({'message': 'Not all SWIM questions are done'}), 200
    
def check_and_update_sem_notification(user_id, db):
    user = models.Utilisateur_EFREI.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Supposez que ID_Formulaire pour SWIM est une constante connue
    SWIM_FORMULAIRE_ID = 2  # Remplacez par l'ID correct du formulaire SWIM

    # Récupérer toutes les questions liées au formulaire SWIM
    questions = db.session.query(models.Question).join(models.Avoir).filter(
        models.Avoir.ID_Formulaire == SWIM_FORMULAIRE_ID
    ).all()

    # Vérifier si toutes les questions sont faites
    all_done = all(question.Faite for question in questions)

    if all_done:
        user.notification_semestre = False
        db.session.commit()
        return jsonify({'message': 'All SEM questions are done. notification_swim set to false'}), 200
    else:
        return jsonify({'message': 'Not all SEM questions are done'}), 200
    