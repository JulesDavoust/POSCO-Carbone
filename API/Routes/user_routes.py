from Functions.user_functions import signin, register
from flask import jsonify, request

def init_user_routes(app, db):
    @app.route('/user/signin', methods=['POST'])
    def post_signin():
        try:
            data = request.get_json()
            res = signin(data, app)
            return jsonify(res)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @app.route('/user/register', methods=['POST'])
    def post_register():
        try:
            data = request.get_json()
            res = register(data, db)
            return jsonify(res)
        except Exception as e:
            return jsonify({"error": str(e)}), 500