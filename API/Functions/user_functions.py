from flask import jsonify
import Models.models as models
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import jwt
import re

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
        'MotDePasse_Utilisateur': generate_password_hash(data['passwordUser'])
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
        return {'message': 'Registered'}, 200
    except Exception as e:
        print("Error during registration: ", str(e))
        return {'message': str(e) or 'Some error occurred while creating the new user.'}, 500
