import Functions.formulaire_functions as fc
from flask import abort, jsonify, request
from middleware.authMiddleware import verify_token
from Models.models import Question, Formulaire, Avoir, Reponse, Répondre, Remplir

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
        
    # Fonctions CRUD pour Formulaire
    @app.route('/formulaires', methods=['POST'])
    def create_formulaire():
        data = request.get_json()
        new_formulaire = Formulaire(
            Nom_Formulaire=data['Nom_Formulaire'],
            Description_Formulaire=data['Description_Formulaire']
        )
        db.session.add(new_formulaire)
        db.session.commit()
        return jsonify({'message': 'Formulaire created successfully'}), 201

    @app.route('/formulaires', methods=['GET'])
    def get_formulaires():
        formulaires = Formulaire.query.all()
        output = [{'ID_Formulaire': f.ID_Formulaire, 'Nom_Formulaire': f.Nom_Formulaire, 'Description_Formulaire': f.Description_Formulaire} for f in formulaires]
        return jsonify(output)

    @app.route('/formulaires/<id>', methods=['GET'])
    def get_formulaire(id):
        formulaire = Formulaire.query.get_or_404(id)
        return jsonify({'ID_Formulaire': formulaire.ID_Formulaire, 'Nom_Formulaire': formulaire.Nom_Formulaire, 'Description_Formulaire': formulaire.Description_Formulaire})

    @app.route('/formulaires/<id>', methods=['PUT'])
    def update_formulaire(id):
        data = request.get_json()
        formulaire = Formulaire.query.get_or_404(id)
        formulaire.Nom_Formulaire = data['Nom_Formulaire']
        formulaire.Description_Formulaire = data['Description_Formulaire']
        db.session.commit()
        return jsonify({'message': 'Formulaire updated successfully'})

    @app.route('/formulaires/<id>', methods=['DELETE'])
    def delete_formulaire(id):
        formulaire = Formulaire.query.get_or_404(id)
        db.session.delete(formulaire)
        db.session.commit()
        return jsonify({'message': 'Formulaire deleted successfully'})
    
    # Fonctions CRUD pour Avoir
    @app.route('/avoir', methods=['POST'])
    def create_avoir():
        data = request.get_json()
        new_avoir = Avoir(
            ID_Question=data['ID_Question'],
            ID_Formulaire=data['ID_Formulaire']
        )
        db.session.add(new_avoir)
        db.session.commit()
        return jsonify({'message': 'Avoir created successfully'}), 201

    @app.route('/avoir', methods=['GET'])
    def get_avoir():
        avoir_list = Avoir.query.all()
        output = [{'ID_Question': a.ID_Question, 'ID_Formulaire': a.ID_Formulaire} for a in avoir_list]
        return jsonify(output)

    @app.route('/avoir/<ID_Question>/<ID_Formulaire>', methods=['GET'])
    def get_avoir_item(ID_Question, ID_Formulaire):
        avoir = Avoir.query.get_or_404((ID_Question, ID_Formulaire))
        return jsonify({'ID_Question': avoir.ID_Question, 'ID_Formulaire': avoir.ID_Formulaire})

    @app.route('/avoir/<ID_Question>/<ID_Formulaire>', methods=['PUT'])
    def update_avoir(ID_Question, ID_Formulaire):
        data = request.get_json()
        avoir = Avoir.query.get_or_404((ID_Question, ID_Formulaire))
        avoir.ID_Question = data['ID_Question']
        avoir.ID_Formulaire = data['ID_Formulaire']
        db.session.commit()
        return jsonify({'message': 'Avoir updated successfully'})

    @app.route('/avoir/<ID_Question>/<ID_Formulaire>', methods=['DELETE'])
    def delete_avoir(ID_Question, ID_Formulaire):
        avoir = Avoir.query.get_or_404((ID_Question, ID_Formulaire))
        db.session.delete(avoir)
        db.session.commit()
        return jsonify({'message': 'Avoir deleted successfully'})
    
    
    # Fonctions CRUD pour Question
    @app.route('/questions', methods=['POST'])
    def create_question():
        data = request.get_json()
        new_question = Question(
            Texte=data['Texte'],
            Type=data['Type'],
            Catégorie=data['Catégorie'],
            Faite=data['Faite']
        )
        db.session.add(new_question)
        db.session.commit()
        return jsonify({'message': 'Question created successfully'}), 201

    @app.route('/questions', methods=['GET'])
    def get_questions():
        questions = Question.query.all()
        output = [{'ID_Question': q.ID_Question, 'Texte': q.Texte, 'Type': q.Type, 'Catégorie': q.Catégorie, 'Faite': q.Faite} for q in questions]
        return jsonify(output)

    @app.route('/questions/<id>', methods=['GET'])
    def get_question(id):
        question = Question.query.get_or_404(id)
        return jsonify({'ID_Question': question.ID_Question, 'Texte': question.Texte, 'Type': question.Type, 'Catégorie': question.Catégorie, 'Faite': question.Faite})

    @app.route('/questions/<id>', methods=['PUT'])
    def update_question(id):
        data = request.get_json()
        question = Question.query.get_or_404(id)
        question.Texte = data['Texte']
        question.Type = data['Type']
        question.Catégorie = data['Catégorie']
        question.Faite = data['Faite']
        db.session.commit()
        return jsonify({'message': 'Question updated successfully'})

    @app.route('/questions/<id>', methods=['DELETE'])
    def delete_question(id):
        question = Question.query.get_or_404(id)
        db.session.delete(question)
        db.session.commit()
        return jsonify({'message': 'Question deleted successfully'})
    
    
    # Fonctions CRUD pour Reponse
    @app.route('/reponses', methods=['POST'])
    def create_reponse():
        data = request.get_json()
        new_reponse = Reponse(
            Texte_reponse=data['Texte_reponse'],
            Type=data['Type'],
            Catégorie=data['Catégorie'],
            ID_Question=data['ID_Question'],
            ID_EmissionCO2=data.get('ID_EmissionCO2')  # Utiliser get pour les valeurs facultatives
        )
        db.session.add(new_reponse)
        db.session.commit()
        return jsonify({'message': 'Reponse created successfully'}), 201

    @app.route('/reponses', methods=['GET'])
    def get_reponses():
        reponses = Reponse.query.all()
        output = [{'ID_Reponse': r.ID_Reponse, 'Texte_reponse': r.Texte_reponse, 'Type': r.Type, 'Catégorie': r.Catégorie, 'ID_Question': r.ID_Question, 'ID_EmissionCO2': r.ID_EmissionCO2} for r in reponses]
        return jsonify(output)

    @app.route('/reponses/<id>', methods=['GET'])
    def get_reponse(id):
        reponse = Reponse.query.get_or_404(id)
        return jsonify({'ID_Reponse': reponse.ID_Reponse, 'Texte_reponse': reponse.Texte_reponse, 'Type': reponse.Type, 'Catégorie': reponse.Catégorie, 'ID_Question': reponse.ID_Question, 'ID_EmissionCO2': reponse.ID_EmissionCO2})

    @app.route('/reponses/<id>', methods=['PUT'])
    def update_reponse(id):
        data = request.get_json()
        reponse = Reponse.query.get_or_404(id)
        reponse.Texte_reponse = data['Texte_reponse']
        reponse.Type = data['Type']
        reponse.Catégorie = data['Catégorie']
        reponse.ID_Question = data['ID_Question']
        reponse.ID_EmissionCO2 = data.get('ID_EmissionCO2')  # Utiliser get pour les valeurs facultatives
        db.session.commit()
        return jsonify({'message': 'Reponse updated successfully'})

    @app.route('/reponses/<id>', methods=['DELETE'])
    def delete_reponse(id):
        reponse = Reponse.query.get_or_404(id)
        db.session.delete(reponse)
        db.session.commit()
        return jsonify({'message': 'Reponse deleted successfully'})
    
    # # get les reponse d'un utilisateur
    # @app.route('/reponses/user/<id>', methods=['GET'])
    # def get_reponse_user(id):
    #     reponses = Reponse.query.filter_by(ID_User=id).all()
    #     output = [{'ID_Reponse': r.ID_Reponse, 'Texte_reponse': r.Texte_reponse, 'Type': r.Type, 'Catégorie': r.Catégorie, 'ID_Question': r.ID_Question, 'ID_EmissionCO2': r.ID_EmissionCO2} for r in reponses]
    #     return jsonify(output)
    
    @app.route('/reponses_par_question/<int:id_question>', methods=['GET'])
    def get_reponses_par_question(id_question):
        reponses = Reponse.query.filter_by(ID_Question=id_question).all()
        return jsonify([reponse_to_dict(reponse) for reponse in reponses])

    def reponse_to_dict(reponse):
        return {
            'ID_Reponse': reponse.ID_Reponse,
            'Texte_reponse': reponse.Texte_reponse,
            'Type': reponse.Type,
            'Catégorie': reponse.Catégorie,
            'ID_Question': reponse.ID_Question,
            'ID_EmissionCO2': reponse.ID_EmissionCO2
        }


    # Read a specific response
    @app.route('/repondre/<int:id_question>', methods=['GET'])
    @verify_token
    def get_repondre(id_question):
        reponse = Répondre.query.get((request.user_id, id_question))
        if not reponse:
            abort(404)
        
        return jsonify({
            'Num_Utilisateur': reponse.request.user_id,
            'ID_Question': reponse.ID_Question,
            'Faite': reponse.Faite
        })

    # Update a specific response
    @app.route('/repondre/<int:id_question>', methods=['PUT'])
    @verify_token
    def update_repondre(id_question):
        reponse = Répondre.query.get((request.user_id, id_question))
        if not reponse:
            abort(404)
        
        if not request.json:
            abort(400)
        
        reponse.Faite = request.json.get('Faite', reponse.Faite)
        db.session.commit()
        
        return jsonify({
            'Num_Utilisateur': reponse.request.user_id,
            'ID_Question': reponse.ID_Question,
            'Faite': reponse.Faite
        })

    # Delete a specific response
    @app.route('/repondre/<int:id_question>', methods=['DELETE'])
    @verify_token
    def delete_repondre(id_question):
        reponse = Répondre.query.get((request.user_id, id_question))
        if not reponse:
            abort(404)
        
        db.session.delete(reponse)
        db.session.commit()
        
        return jsonify({'result': True})


    @app.route('/question_non_repondue', methods=['GET'])
    @verify_token
    def get_question_non_repondue():
        # Récupérer l'ID de l'utilisateur à partir de la requête
        num_utilisateur = request.user_id

        # Requête pour trouver les questions non répondues par l'utilisateur
        question_non_repondue = db.session.query(Question).join(
            Répondre, 
            (Question.ID_Question == Répondre.ID_Question) & 
            (Répondre.Num_Utilisateur == num_utilisateur) & 
            (Répondre.Faite == False)
        ).all()
        print(question_non_repondue)
        if question_non_repondue:
            result = [{
                'ID_Question': question.ID_Question,
                'Texte': question.Texte,
                'Type': question.Type,
                'Catégorie': question.Catégorie
            } for question in question_non_repondue]
            return jsonify(result)
        else:
            return jsonify({'message': 'Toutes les questions ont été répondues par cet utilisateur.'}), 404


        
    # Fonctions CRUD pour Remplir
    @app.route('/remplir', methods=['POST'])
    def create_remplir():
        data = request.get_json()
        new_remplir = Remplir(
            Num_Utilisateur=data['Num_Utilisateur'],
            ID_Formulaire=data['ID_Formulaire']
        )
        db.session.add(new_remplir)
        db.session.commit()
        return jsonify({'message': 'Remplir created successfully'}), 201

    @app.route('/remplir', methods=['GET'])
    def get_remplir():
        remplir_list = Remplir.query.all()
        output = [{'Num_Utilisateur': r.Num_Utilisateur, 'ID_Formulaire': r.ID_Formulaire} for r in remplir_list]
        return jsonify(output)

    @app.route('/remplir/<ID_Formulaire>', methods=['GET'])
    @verify_token
    def get_remplir_item(ID_Formulaire):
        remplir = Remplir.query.get_or_404((request.user_id, ID_Formulaire))
        return jsonify({'Num_Utilisateur': remplir.request.user_id, 'ID_Formulaire': remplir.ID_Formulaire})



    @app.route('/remplir/<ID_Formulaire>', methods=['DELETE'])
    @verify_token
    def delete_remplir(ID_Formulaire):
        remplir = Remplir.query.get_or_404((request.user_id, ID_Formulaire))
        db.session.delete(remplir)
        db.session.commit()
        return jsonify({'message': 'Remplir deleted successfully'})