from Functions.user_functions import signin, register, set_notification_swim, set_notification_semestre, send_notifications, check_and_update_swim_notification, check_and_update_sem_notification
from flask import jsonify, request
from middleware.authMiddleware import verify_token
from Models.models import Utilisateur_EFREI, Conseil, Donner, Promotion

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
        
        
    # Fonctions CRUD pour Utilisateur_EFREI
    @app.route('/utilisateurs', methods=['POST'])
    def create_utilisateur():
        data = request.get_json()
        new_utilisateur = Utilisateur_EFREI(
            Nom=data['Nom'],
            Prénom=data['Prénom'],
            Email=data['Email'],
            MotDePasse_Utilisateur=data['MotDePasse_Utilisateur'],
            ID_Promotion=data['ID_Promotion']
        )
        db.session.add(new_utilisateur)
        db.session.commit()
        return jsonify({'message': 'Utilisateur_EFREI created successfully'}), 201


    @app.route('/utilisateurs', methods=['GET'])
    @verify_token
    def get_utilisateur():
        utilisateur = Utilisateur_EFREI.query.get_or_404(request.user_id)
        return jsonify({'Num_Utilisateur': utilisateur.Num_Utilisateur, 'Nom': utilisateur.Nom, 'Prénom': utilisateur.Prénom, 'Email': utilisateur.Email, 'MotDePasse_Utilisateur': utilisateur.MotDePasse_Utilisateur, 'ID_Promotion': utilisateur.ID_Promotion})

    @app.route('/utilisateurs', methods=['PUT'])
    @verify_token
    def update_utilisateur():
        data = request.get_json()
        utilisateur = Utilisateur_EFREI.query.get_or_404(request.user_id)
        utilisateur.Nom = data['Nom']
        utilisateur.Prénom = data['Prénom']
        utilisateur.Email = data['Email']
        utilisateur.MotDePasse_Utilisateur = data['MotDePasse_Utilisateur']
        utilisateur.ID_Promotion = data['ID_Promotion']
        db.session.commit()
        return jsonify({'message': 'Utilisateur_EFREI updated successfully'})

    @app.route('/utilisateurs', methods=['DELETE'])
    @verify_token
    def delete_utilisateur():
        utilisateur = Utilisateur_EFREI.query.get_or_404(request.user_id)
        db.session.delete(utilisateur)
        db.session.commit()
        return jsonify({'message': 'Utilisateur_EFREI deleted successfully'})
    
    
    # Fonctions CRUD pour Conseil
    @app.route('/conseils', methods=['POST'])
    def create_conseil():
        data = request.get_json()
        new_conseil = Conseil(
            Texte=data['Texte'],
            Catégorie=data['Catégorie']
        )
        db.session.add(new_conseil)
        db.session.commit()
        return jsonify({'message': 'Conseil created successfully'}), 201

    @app.route('/conseils', methods=['GET'])
    def get_conseils():
        conseils = Conseil.query.all()
        output = [{'ID_Conseil': c.ID_Conseil, 'Texte': c.Texte, 'Catégorie': c.Catégorie} for c in conseils]
        return jsonify(output)

    @app.route('/conseils/<id>', methods=['GET'])
    def get_conseil(id):
        conseil = Conseil.query.get_or_404(id)
        return jsonify({'ID_Conseil': conseil.ID_Conseil, 'Texte': conseil.Texte, 'Catégorie': conseil.Catégorie})

    @app.route('/conseils/<id>', methods=['PUT'])
    def update_conseil(id):
        data = request.get_json()
        conseil = Conseil.query.get_or_404(id)
        conseil.Texte = data['Texte']
        conseil.Catégorie = data['Catégorie']
        db.session.commit()
        return jsonify({'message': 'Conseil updated successfully'})

    @app.route('/conseils/<id>', methods=['DELETE'])
    def delete_conseil(id):
        conseil = Conseil.query.get_or_404(id)
        db.session.delete(conseil)
        db.session.commit()
        return jsonify({'message': 'Conseil deleted successfully'})
    
    @app.route('/conseils_par_categorie/<string:categorie>', methods=['GET'])
    def get_conseils_par_categorie(categorie):
        conseils = Conseil.query.filter_by(Catégorie=categorie).all()
        return jsonify([conseil_to_dict(conseil) for conseil in conseils])

    def conseil_to_dict(conseil):
        return {
            'ID_Conseil': conseil.ID_Conseil,
            'Texte': conseil.Texte,
            'Catégorie': conseil.Catégorie
    }
    
    
    # Fonctions CRUD pour Donner
    @app.route('/donner', methods=['POST'])
    def create_donner():
        data = request.get_json()
        new_donner = Donner(
            Num_Utilisateur=data['Num_Utilisateur'],
            ID_Conseil=data['ID_Conseil']
        )
        db.session.add(new_donner)
        db.session.commit()
        return jsonify({'message': 'Donner created successfully'}), 201

    @app.route('/donner', methods=['GET'])
    def get_donner():
        donner_list = Donner.query.all()
        output = [{'Num_Utilisateur': d.Num_Utilisateur, 'ID_Conseil': d.ID_Conseil} for d in donner_list]
        return jsonify(output)

    @app.route('/donner/<ID_Conseil>', methods=['GET'])
    @verify_token
    def get_donner_item(ID_Conseil):
        donner = Donner.query.get_or_404((request.user_id, ID_Conseil))
        return jsonify({'Num_Utilisateur': donner.request.user_id, 'ID_Conseil': donner.ID_Conseil})

    @app.route('/donner/<ID_Conseil>', methods=['PUT'])
    @verify_token
    def update_donner(ID_Conseil):
        data = request.get_json()
        donner = Donner.query.get_or_404((request.user_id, ID_Conseil))
        donner.Num_Utilisateur = data['Num_Utilisateur']
        donner.ID_Conseil = data['ID_Conseil']
        db.session.commit()
        return jsonify({'message': 'Donner updated successfully'})

    @app.route('/donner/<ID_Conseil>', methods=['DELETE'])
    @verify_token
    def delete_donner(ID_Conseil):
        donner = Donner.query.get_or_404((request.user_id, ID_Conseil))
        db.session.delete(donner)
        db.session.commit()
        return jsonify({'message': 'Donner deleted successfully'})
    
    
    # Fonctions CRUD pour Promotion
    @app.route('/promotions', methods=['POST'])
    def create_promotion():
        data = request.get_json()
        new_promotion = Promotion(
            Année=data['Année']
        )
        db.session.add(new_promotion)
        db.session.commit()
        return jsonify({'message': 'Promotion created successfully'}), 201

    @app.route('/promotions', methods=['GET'])
    def get_promotions():
        promotions = Promotion.query.all()
        output = [{'ID_Promotion': p.ID_Promotion, 'Année': p.Année} for p in promotions]
        return jsonify(output)

    @app.route('/promotions/<id>', methods=['GET'])
    def get_promotion(id):
        promotion = Promotion.query.get_or_404(id)
        return jsonify({'ID_Promotion': promotion.ID_Promotion, 'Année': promotion.Année})

    @app.route('/promotions/<id>', methods=['PUT'])
    def update_promotion(id):
        data = request.get_json()
        promotion = Promotion.query.get_or_404(id)
        promotion.Année = data['Année']
        db.session.commit()
        return jsonify({'message': 'Promotion updated successfully'})

    @app.route('/promotions/<id>', methods=['DELETE'])
    def delete_promotion(id):
        promotion = Promotion.query.get_or_404(id)
        db.session.delete(promotion)
        db.session.commit()
        return jsonify({'message': 'Promotion deleted successfully'})
