from flask import jsonify, request, current_app
import jwt
from functools import wraps

def verify_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')

        if not token:
            return {'message': 'No token provided!'}, 403

        try:
            decoded = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return {'message': 'Token has expired!'}, 401
        except jwt.InvalidTokenError:
            return {'message': 'Invalid token!'}, 401

        request.user_id = decoded.get('userID')
        # request.admin = decoded.get('isAdmin')
        return f(*args, **kwargs)
    return decorated