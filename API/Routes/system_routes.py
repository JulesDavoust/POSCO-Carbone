import Functions.system_functions
from flask import jsonify, request

def init_system_routes(app):
    @app.route('/', methods=['GET'])
    def get_main():
        try:
            hello = Functions.system_functions.main()
            return jsonify(hello)
        except Exception as e:
            return jsonify({"error": str(e)}), 500