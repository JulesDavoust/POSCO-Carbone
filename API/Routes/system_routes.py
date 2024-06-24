import Functions.system_functions
from middleware.authMiddleware import verify_token
from flask import jsonify, request

def init_system_routes(app):
    @app.route('/', methods=['GET'])
    @verify_token
    def get_main():
        try:
            print('test')
            print(request.user_id)
            hello = Functions.system_functions.main()
            return jsonify(hello)
        except Exception as e:
            return jsonify({"error": str(e)}), 500