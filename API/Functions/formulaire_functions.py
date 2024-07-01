import Models.models as models
import jwt
from flask import Flask, request, jsonify, redirect
import logging

def access_questionnaire(app, token):
    if not token:
        return jsonify({'message': 'Token is missing'}), 400

    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])

        user = models.Utilisateur_EFREI.query.get(payload['user_id'])
        if not user:
            return jsonify({'message': 'User not found'}), 400

        if payload['type'] == 'swim':
            if user.token_swim != token or payload.get('completed', False):
                return jsonify({'message': 'Token has already been used or is invalid'}), 400
        elif payload['type'] == 'semestre':
            if user.token_semestre != token or payload.get('completed', False):
                return jsonify({'message': 'Token has already been used or is invalid'}), 400

        return jsonify({'message': 'Token is valid', 'user_id': payload['user_id'], 'type': payload['type']}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 400
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 400

def complete_questionnaire(app, token, db):
    if not token:
        return jsonify({'message': 'Token is missing'}), 400

    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])

        user = models.Utilisateur_EFREI.query.get(payload['user_id'])
        if not user:
            return jsonify({'message': 'User not found'}), 400

        if payload['type'] == 'swim':
            if user.token_swim != token:
                return jsonify({'message': 'Invalid token'}), 400
            user.token_swim = None
        elif payload['type'] == 'semestre':
            if user.token_semestre != token:
                return jsonify({'message': 'Invalid token'}), 400
            user.token_semestre = None

        payload['completed'] = True
        new_token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        db.session.commit()

        return jsonify({'message': 'Questionnaire completed', 'new_token': new_token}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 400
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 400
