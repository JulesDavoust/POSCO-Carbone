import Functions.formulaire_functions as fc
from flask import jsonify, request
from middleware.authMiddleware import verify_token


def init_formulaire_routes(app, db):
    route_init = 0

    @app.route('/questionnaire', methods=['GET'])
    def get_access_questionnaire():
        token = request.args.get('token')
        print('route 1', token)
        print(token)
        return fc.access_questionnaire(app, token)
    
    @app.route('/questionnaire/complete', methods=['POST'])
    def post_complete_questionnaire():
        data = request.get_json()
        print("route",data)
        token = data.get('token')
        print('route token', token)
        print(token)
        return fc.complete_questionnaire(app, token, db)