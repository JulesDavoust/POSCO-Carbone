from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

app = Flask(__name__)

# Configurer la base de données MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://root:adminadmin@localhost/posco')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Question(db.Model):
    __tablename__ = 'Question'
    ID_Question = db.Column(db.Integer, primary_key=True)
    Texte = db.Column(db.String(150))
    Type = db.Column(db.String(50))
    Catégorie = db.Column(db.String(50))
    Faite = db.Column(db.Boolean)

class Formulaire(db.Model):
    __tablename__ = 'Formulaire'
    ID_Formulaire = db.Column(db.Integer, primary_key=True)
    Nom_Formulaire = db.Column(db.String(50))
    Description_Formulaire = db.Column(db.String(250))

class EmissionCO2(db.Model):
    __tablename__ = 'EmissionCO2'
    ID_EmissionCO2 = db.Column(db.Integer, primary_key=True)
    Element_EmissionCO2 = db.Column(db.String(50))
    Coefficient_EmissionCO2 = db.Column(db.Numeric(15, 2))

class BilanCarbone(db.Model):
    __tablename__ = 'BilanCarbone'
    ID_BilanCarbone = db.Column(db.Integer, primary_key=True)
    BilanTotal = db.Column(db.Numeric(15, 2))
    BilanCatégorie = db.Column(db.Numeric(15, 2))
    Date_BilanCarbone = db.Column(db.Date)
    ID_Formulaire = db.Column(db.Integer, db.ForeignKey('Formulaire.ID_Formulaire'), unique=True, nullable=False)
    formulaire = db.relationship('Formulaire', backref=db.backref('bilan_carbone', uselist=False))

class Conseil(db.Model):
    __tablename__ = 'Conseil'
    ID_Conseil = db.Column(db.Integer, primary_key=True)
    Texte = db.Column(db.String(200))
    Catégorie = db.Column(db.String(100))

class Promotion(db.Model):
    __tablename__ = 'Promotion'
    ID_Promotion = db.Column(db.Integer, primary_key=True)
    Année = db.Column(db.String(50))

class Reponse(db.Model):
    __tablename__ = 'Reponse'
    ID_Reponse = db.Column(db.Integer, primary_key=True)
    Texte_reponse = db.Column(db.String(500))
    Type = db.Column(db.String(50))
    Catégorie = db.Column(db.String(50))
    ID_Question = db.Column(db.Integer, db.ForeignKey('Question.ID_Question'), nullable=False)
    ID_EmissionCO2 = db.Column(db.Integer, db.ForeignKey('EmissionCO2.ID_EmissionCO2'))
    question = db.relationship('Question', backref=db.backref('reponses', lazy=True))
    emission_co2 = db.relationship('EmissionCO2', backref=db.backref('reponses', lazy=True))

class UtilisateurEFREI(db.Model):
    __tablename__ = 'Utilisateur_EFREI'
    Num_Utilisateur = db.Column(db.Integer, primary_key=True)
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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
