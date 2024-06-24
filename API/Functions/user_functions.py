from flask import jsonify
import Models.models as models
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import jwt
import re

def signin(data, app):

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email and password are required!'}), 400

    user = models.Utilisateur_EFREI.query.filter_by(email=data['email']).first()

    if not user:
        return jsonify({'message': 'User Not found.'}), 404

    if not check_password_hash(user.password, data['password']):
        return jsonify({'accessToken': None, 'message': 'Invalid Password!'}), 401

    token = jwt.encode({
        'userID': user.id,
        # 'isAdmin': user.isAdmin,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({
        'userID': user.id,
        'email': user.email,
        'accessToken': token
    }), 200


def register(data, db):
    email_regex = r'^\S+@\S+\.\S+$'

    if not re.match(email_regex, data.get('email', '')):
        return jsonify({'message': 'Not valid format'}), 500

    if 'password' not in data:
        return jsonify({'message': 'Password is required'}), 400

    new_user = {
        'email': data['email'],
        'password': generate_password_hash(data['password']),
        # 'isAdmin': False
    }

    existing_user = models.Utilisateur_EFREI.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({'message': 'Email already taken'}), 500

    try:
        user = models.Utilisateur_EFREI(**new_user)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Registered'}), 200
    except Exception as e:
        return jsonify({'message': str(e) or 'Some error occurred while creating the new user.'}), 500