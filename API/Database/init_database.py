from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

app = Flask(__name__)

# Configurer la base de données MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://root:root@localhost/posco')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Question(db.Model):
    __tablename__ = 'Question'
    ID_Question = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Texte = db.Column(db.String(150))
    Type = db.Column(db.String(50))
    Catégorie = db.Column(db.String(50))
    Faite = db.Column(db.Boolean)

class Formulaire(db.Model):
    __tablename__ = 'Formulaire'
    ID_Formulaire = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nom_Formulaire = db.Column(db.String(50))
    Description_Formulaire = db.Column(db.String(250))

class EmissionCO2(db.Model):
    __tablename__ = 'EmissionCO2'
    ID_EmissionCO2 = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Element_EmissionCO2 = db.Column(db.String(50))
    Coefficient_EmissionCO2 = db.Column(db.Numeric(15, 2))

class BilanCarbone(db.Model):
    __tablename__ = 'BilanCarbone'
    ID_BilanCarbone = db.Column(db.Integer, primary_key=True, autoincrement=True)
    BilanTotal = db.Column(db.Numeric(15, 2))
    BilanCatégorie = db.Column(db.Numeric(15, 2))
    Date_BilanCarbone = db.Column(db.Date)
    ID_Formulaire = db.Column(db.Integer, db.ForeignKey('Formulaire.ID_Formulaire'), unique=True, nullable=False)
    formulaire = db.relationship('Formulaire', backref=db.backref('bilan_carbone', uselist=False))

class Conseil(db.Model):
    __tablename__ = 'Conseil'
    ID_Conseil = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Texte = db.Column(db.String(200))
    Catégorie = db.Column(db.String(100))

class Promotion(db.Model):
    __tablename__ = 'Promotion'
    ID_Promotion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Année = db.Column(db.String(50))

class Reponse(db.Model):
    __tablename__ = 'Reponse'
    ID_Reponse = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Texte_reponse = db.Column(db.String(500))
    Type = db.Column(db.String(50))
    Catégorie = db.Column(db.String(50))
    ID_Question = db.Column(db.Integer, db.ForeignKey('Question.ID_Question'), nullable=False)
    ID_EmissionCO2 = db.Column(db.Integer, db.ForeignKey('EmissionCO2.ID_EmissionCO2'))
    question = db.relationship('Question', backref=db.backref('reponses', lazy=True))
    emission_co2 = db.relationship('EmissionCO2', backref=db.backref('reponses', lazy=True))

class UtilisateurEFREI(db.Model):
    __tablename__ = 'Utilisateur_EFREI'
    Num_Utilisateur = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nom = db.Column(db.String(50))
    Prénom = db.Column(db.String(50))
    Email = db.Column(db.String(60))
    MotDePasse_Utilisateur = db.Column(db.String(1000))
    ID_Promotion = db.Column(db.Integer, db.ForeignKey('Promotion.ID_Promotion'))
    promotion = db.relationship('Promotion', backref=db.backref('utilisateurs', lazy=True))

class Remplir(db.Model):
    __tablename__ = 'Remplir'
    Num_Utilisateur = db.Column(db.Integer, db.ForeignKey('Utilisateur_EFREI.Num_Utilisateur'), primary_key=True)
    ID_Formulaire = db.Column(db.Integer, db.ForeignKey('Formulaire.ID_Formulaire'), primary_key=True)
    utilisateur = db.relationship('UtilisateurEFREI', backref=db.backref('remplir', lazy=True))
    formulaire = db.relationship('Formulaire', backref=db.backref('remplir', lazy=True))

class Avoir(db.Model):
    __tablename__ = 'Avoir'
    ID_Question = db.Column(db.Integer, db.ForeignKey('Question.ID_Question'), primary_key=True)
    ID_Formulaire = db.Column(db.Integer, db.ForeignKey('Formulaire.ID_Formulaire'), primary_key=True)
    question = db.relationship('Question', backref=db.backref('avoir', lazy=True))
    formulaire = db.relationship('Formulaire', backref=db.backref('avoir', lazy=True))

class Contenir(db.Model):
    __tablename__ = 'Contenir'
    ID_EmissionCO2 = db.Column(db.Integer, db.ForeignKey('EmissionCO2.ID_EmissionCO2'), primary_key=True)
    ID_BilanCarbone = db.Column(db.Integer, db.ForeignKey('BilanCarbone.ID_BilanCarbone'), primary_key=True)
    emission_co2 = db.relationship('EmissionCO2', backref=db.backref('contenir', lazy=True))
    bilan_carbone = db.relationship('BilanCarbone', backref=db.backref('contenir', lazy=True))

class Donner(db.Model):
    __tablename__ = 'Donner'
    Num_Utilisateur = db.Column(db.Integer, db.ForeignKey('Utilisateur_EFREI.Num_Utilisateur'), primary_key=True)
    ID_Conseil = db.Column(db.Integer, db.ForeignKey('Conseil.ID_Conseil'), primary_key=True)
    utilisateur = db.relationship('UtilisateurEFREI', backref=db.backref('donner', lazy=True))
    conseil = db.relationship('Conseil', backref=db.backref('donner', lazy=True))


with app.app_context():
    db.create_all()

    
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

# Fonctions CRUD pour BilanCarbone
@app.route('/bilans', methods=['POST'])
def create_bilan():
    data = request.get_json()
    new_bilan = BilanCarbone(
        BilanTotal=data['BilanTotal'],
        BilanCatégorie=data['BilanCatégorie'],
        Date_BilanCarbone=data['Date_BilanCarbone'],
        ID_Formulaire=data['ID_Formulaire']
    )
    db.session.add(new_bilan)
    db.session.commit()
    return jsonify({'message': 'BilanCarbone created successfully'}), 201

@app.route('/bilans', methods=['GET'])
def get_bilans():
    bilans = BilanCarbone.query.all()
    output = [{'ID_BilanCarbone': b.ID_BilanCarbone, 'BilanTotal': b.BilanTotal, 'BilanCatégorie': b.BilanCatégorie, 'Date_BilanCarbone': b.Date_BilanCarbone, 'ID_Formulaire': b.ID_Formulaire} for b in bilans]
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

# Fonctions CRUD pour Utilisateur_EFREI
@app.route('/utilisateurs', methods=['POST'])
def create_utilisateur():
    data = request.get_json()
    new_utilisateur = UtilisateurEFREI(
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
def get_utilisateurs():
    utilisateurs = UtilisateurEFREI.query.all()
    output = [{'Num_Utilisateur': u.Num_Utilisateur, 'Nom': u.Nom, 'Prénom': u.Prénom, 'Email': u.Email, 'MotDePasse_Utilisateur': u.MotDePasse_Utilisateur, 'ID_Promotion': u.ID_Promotion} for u in utilisateurs]
    return jsonify(output)

@app.route('/utilisateurs/<id>', methods=['GET'])
def get_utilisateur(id):
    utilisateur = UtilisateurEFREI.query.get_or_404(id)
    return jsonify({'Num_Utilisateur': utilisateur.Num_Utilisateur, 'Nom': utilisateur.Nom, 'Prénom': utilisateur.Prénom, 'Email': utilisateur.Email, 'MotDePasse_Utilisateur': utilisateur.MotDePasse_Utilisateur, 'ID_Promotion': utilisateur.ID_Promotion})

@app.route('/utilisateurs/<id>', methods=['PUT'])
def update_utilisateur(id):
    data = request.get_json()
    utilisateur = UtilisateurEFREI.query.get_or_404(id)
    utilisateur.Nom = data['Nom']
    utilisateur.Prénom = data['Prénom']
    utilisateur.Email = data['Email']
    utilisateur.MotDePasse_Utilisateur = data['MotDePasse_Utilisateur']
    utilisateur.ID_Promotion = data['ID_Promotion']
    db.session.commit()
    return jsonify({'message': 'Utilisateur_EFREI updated successfully'})

@app.route('/utilisateurs/<id>', methods=['DELETE'])
def delete_utilisateur(id):
    utilisateur = UtilisateurEFREI.query.get_or_404(id)
    db.session.delete(utilisateur)
    db.session.commit()
    return jsonify({'message': 'Utilisateur_EFREI deleted successfully'})

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

@app.route('/remplir/<Num_Utilisateur>/<ID_Formulaire>', methods=['GET'])
def get_remplir_item(Num_Utilisateur, ID_Formulaire):
    remplir = Remplir.query.get_or_404((Num_Utilisateur, ID_Formulaire))
    return jsonify({'Num_Utilisateur': remplir.Num_Utilisateur, 'ID_Formulaire': remplir.ID_Formulaire})

@app.route('/remplir/<Num_Utilisateur>/<ID_Formulaire>', methods=['PUT'])
def update_remplir(Num_Utilisateur, ID_Formulaire):
    data = request.get_json()
    remplir = Remplir.query.get_or_404((Num_Utilisateur, ID_Formulaire))
    remplir.Num_Utilisateur = data['Num_Utilisateur']
    remplir.ID_Formulaire = data['ID_Formulaire']
    db.session.commit()
    return jsonify({'message': 'Remplir updated successfully'})

@app.route('/remplir/<Num_Utilisateur>/<ID_Formulaire>', methods=['DELETE'])
def delete_remplir(Num_Utilisateur, ID_Formulaire):
    remplir = Remplir.query.get_or_404((Num_Utilisateur, ID_Formulaire))
    db.session.delete(remplir)
    db.session.commit()
    return jsonify({'message': 'Remplir deleted successfully'})

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

@app.route('/donner/<Num_Utilisateur>/<ID_Conseil>', methods=['GET'])
def get_donner_item(Num_Utilisateur, ID_Conseil):
    donner = Donner.query.get_or_404((Num_Utilisateur, ID_Conseil))
    return jsonify({'Num_Utilisateur': donner.Num_Utilisateur, 'ID_Conseil': donner.ID_Conseil})

@app.route('/donner/<Num_Utilisateur>/<ID_Conseil>', methods=['PUT'])
def update_donner(Num_Utilisateur, ID_Conseil):
    data = request.get_json()
    donner = Donner.query.get_or_404((Num_Utilisateur, ID_Conseil))
    donner.Num_Utilisateur = data['Num_Utilisateur']
    donner.ID_Conseil = data['ID_Conseil']
    db.session.commit()
    return jsonify({'message': 'Donner updated successfully'})

@app.route('/donner/<Num_Utilisateur>/<ID_Conseil>', methods=['DELETE'])
def delete_donner(Num_Utilisateur, ID_Conseil):
    donner = Donner.query.get_or_404((Num_Utilisateur, ID_Conseil))
    db.session.delete(donner)
    db.session.commit()
    return jsonify({'message': 'Donner deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
