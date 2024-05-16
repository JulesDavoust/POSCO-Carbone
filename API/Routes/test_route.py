from Functions.test_function import AllPlateforms
from flask import jsonify, request

def init_routes_test_route(app):
    @app.route('/getAllPlateforms', methods=['GET'])
    def get_all_plateforms():
        try:
            plateforms = AllPlateforms()
            plateforms_list = [{'namePlateform': plateform.namePlateform} for plateform in plateforms]
            return jsonify(plateforms_list)
        except Exception as e:
            return jsonify({"error": str(e)}), 500