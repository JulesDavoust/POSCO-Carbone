import Functions.co2_functions
from flask import jsonify, request
from middleware.authMiddleware import verify_token
from Models.models import EmissionCO2, Contenir, BilanCarbone, Reponse

def init_co2_routes(app, db):
    route_init = 0

    # Fonctions CRUD pour EmissionCO2
    @app.route('/emissions', methods=['POST'])
    def create_emission():
        data = request.get_json()
        new_emission = EmissionCO2(
            Element_EmissionCO2=data['Element_EmissionCO2'],
            Coefficient_EmissionCO2=data['Coefficient_EmissionCO2']
        )
        db.session.add(new_emission)
        db.session.commit()
        return jsonify({'message': 'EmissionCO2 created successfully'}), 201

    @app.route('/emissions', methods=['GET'])
    def get_emissions():
        emissions = EmissionCO2.query.all()
        output = [{'ID_EmissionCO2': e.ID_EmissionCO2, 'Element_EmissionCO2': e.Element_EmissionCO2, 'Coefficient_EmissionCO2': e.Coefficient_EmissionCO2} for e in emissions]
        return jsonify(output)

    @app.route('/emissions/<id>', methods=['GET'])
    def get_emission(id):
        emission = EmissionCO2.query.get_or_404(id)
        return jsonify({'ID_EmissionCO2': emission.ID_EmissionCO2, 'Element_EmissionCO2': emission.Element_EmissionCO2, 'Coefficient_EmissionCO2': emission.Coefficient_EmissionCO2})

    @app.route('/emissions/<id>', methods=['PUT'])
    def update_emission(id):
        data = request.get_json()
        emission = EmissionCO2.query.get_or_404(id)
        emission.Element_EmissionCO2 = data['Element_EmissionCO2']
        emission.Coefficient_EmissionCO2 = data['Coefficient_EmissionCO2']
        db.session.commit()
        return jsonify({'message': 'EmissionCO2 updated successfully'})

    @app.route('/emissions/<id>', methods=['DELETE'])
    def delete_emission(id):
        emission = EmissionCO2.query.get_or_404(id)
        db.session.delete(emission)
        db.session.commit()
        return jsonify({'message': 'EmissionCO2 deleted successfully'})
    
    @app.route('/emission_co2_par_reponse/<int:id_reponse>', methods=['GET'])
    def get_emission_co2_par_reponse(id_reponse):
        reponse = Reponse.query.get(id_reponse)
        if reponse and reponse.ID_EmissionCO2:
            emission_co2 = EmissionCO2.query.get(reponse.ID_EmissionCO2)
            return jsonify(emission_co2_to_dict(emission_co2))
        else:
            return jsonify({'message': 'Emission CO2 non trouvée pour cette réponse.'}), 404

    def emission_co2_to_dict(emission_co2):
        return {
            'ID_EmissionCO2': emission_co2.ID_EmissionCO2,
            'Element_EmissionCO2': emission_co2.Element_EmissionCO2,
            'Coefficient_EmissionCO2': emission_co2.Coefficient_EmissionCO2
        }
    # Fonctions CRUD pour Contenir
    @app.route('/contenir', methods=['POST'])
    def create_contenir():
        data = request.get_json()
        new_contenir = Contenir(
            ID_EmissionCO2=data['ID_EmissionCO2'],
            ID_BilanCarbone=data['ID_BilanCarbone']
        )
        db.session.add(new_contenir)
        db.session.commit()
        return jsonify({'message': 'Contenir created successfully'}), 201

    @app.route('/contenir', methods=['GET'])
    def get_contenir():
        contenir_list = Contenir.query.all()
        output = [{'ID_EmissionCO2': c.ID_EmissionCO2, 'ID_BilanCarbone': c.ID_BilanCarbone} for c in contenir_list]
        return jsonify(output)

    @app.route('/contenir/<ID_EmissionCO2>/<ID_BilanCarbone>', methods=['GET'])
    def get_contenir_item(ID_EmissionCO2, ID_BilanCarbone):
        contenir = Contenir.query.get_or_404((ID_EmissionCO2, ID_BilanCarbone))
        return jsonify({'ID_EmissionCO2': contenir.ID_EmissionCO2, 'ID_BilanCarbone': contenir.ID_BilanCarbone})

    @app.route('/contenir/<ID_EmissionCO2>/<ID_BilanCarbone>', methods=['PUT'])
    def update_contenir(ID_EmissionCO2, ID_BilanCarbone):
        data = request.get_json()
        contenir = Contenir.query.get_or_404((ID_EmissionCO2, ID_BilanCarbone))
        contenir.ID_EmissionCO2 = data['ID_EmissionCO2']
        contenir.ID_BilanCarbone = data['ID_BilanCarbone']
        db.session.commit()
        return jsonify({'message': 'Contenir updated successfully'})

    @app.route('/contenir/<ID_EmissionCO2>/<ID_BilanCarbone>', methods=['DELETE'])
    def delete_contenir(ID_EmissionCO2, ID_BilanCarbone):
        contenir = Contenir.query.get_or_404((ID_EmissionCO2, ID_BilanCarbone))
        db.session.delete(contenir)
        db.session.commit()
        return jsonify({'message': 'Contenir deleted successfully'})
    
    
    # Fonctions CRUD pour BilanCarbone
    @app.route('/bilans', methods=['POST'])
    @verify_token
    def create_bilan():
    
        data = request.get_json()
        new_bilan = BilanCarbone(
            BilanTotal=data['BilanTotal'],
            BilanCatégorie=data['BilanCatégorie'],
            Date_BilanCarbone=data['Date_BilanCarbone'],
            Num_Utilisateur = request.user_id  # Including Num_Utilisateur as a foreign key
        )
        db.session.add(new_bilan)
        db.session.commit()
        return jsonify({'message': 'BilanCarbone created successfully'}), 201

    @app.route('/bilans', methods=['GET'])
    def get_bilans():
        bilans = BilanCarbone.query.all()
        output = [{'ID_BilanCarbone': b.ID_BilanCarbone, 'BilanTotal': b.BilanTotal, 'BilanCatégorie': b.BilanCatégorie, 'Date_BilanCarbone': b.Date_BilanCarbone} for b in bilans]
        return jsonify(output)

    @app.route('/bilans/<id>', methods=['GET'])
    def get_bilan(id):
        bilan = BilanCarbone.query.get_or_404(id)
        return jsonify({'ID_BilanCarbone': bilan.ID_BilanCarbone, 'BilanTotal': bilan.BilanTotal, 'BilanCatégorie': bilan.BilanCatégorie, 'Date_BilanCarbone': bilan.Date_BilanCarbone, 'ID_Formulaire': bilan.ID_Formulaire})

    @app.route('/bilans/<id>', methods=['PUT'])
    def update_bilan(id):
        data = request.get_json()
        bilan = BilanCarbone.query.get_or_404(id)
        bilan.BilanTotal = data['BilanTotal']
        bilan.BilanCatégorie = data['BilanCatégorie']
        bilan.Date_BilanCarbone = data['Date_BilanCarbone']
        bilan.ID_Formulaire = data['ID_Formulaire']
        db.session.commit()
        return jsonify({'message': 'BilanCarbone updated successfully'})

    @app.route('/bilans/<id>', methods=['DELETE'])
    def delete_bilan(id):
        bilan = BilanCarbone.query.get_or_404(id)
        db.session.delete(bilan)
        db.session.commit()
        return jsonify({'message': 'BilanCarbone deleted successfully'})
    
    @app.route('/bilan_carbone_par_utilisateur', methods=['GET'])
    @verify_token
    def get_bilan_carbone_par_utilisateur():
        bilans_carbone = BilanCarbone.query.filter_by(Num_Utilisateur=request.user_id).all()
        return jsonify([bilan.to_dict() for bilan in bilans_carbone])

    def bilan_to_dict(bilan):
        return {
            'ID_BilanCarbone': bilan.ID_BilanCarbone,
            'BilanTotal': bilan.BilanTotal,
            'BilanCatégorie': bilan.BilanCatégorie,
            'Date_BilanCarbone': bilan.Date_BilanCarbone,
            'Num_Utilisateur': bilan.Num_Utilisateur
        }
    BilanCarbone.to_dict = bilan_to_dict
