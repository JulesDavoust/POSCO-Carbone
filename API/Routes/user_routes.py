from Functions.user_functions import signin, register, set_notification_swim, set_notification_semestre, send_notifications, check_and_update_swim_notification, check_and_update_sem_notification
from flask import jsonify, request
from middleware.authMiddleware import verify_token

def init_user_routes(app, db, mail):
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
        
    @app.route('/user/set_notification_swim', methods=['POST'])
    @verify_token
    def post_notification_swim():
        return set_notification_swim(request.user_id, app, db)
    
    @app.route('/user/set_notification_semestre', methods=['POST'])
    @verify_token
    def post_notification_semestre():
        return set_notification_semestre(request.user_id, app, db)
    
    @app.route('/user/sendnotif', methods=['POST'])
    def post_notification():
        send_notifications(app, db, mail)
        return jsonify({'message': 'Notifications sent'}), 200
    
    @app.route('/user/verifnotif_swim', methods=['POST'])
    @verify_token
    def post_verif_notif_swim():
        return check_and_update_swim_notification(request.user_id, db)
    
    @app.route('/user/verifnotif_sem', methods=['POST'])
    @verify_token
    def post_verif_notif_sem():
        return check_and_update_sem_notification(request.user_id, db)