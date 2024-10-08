from Database.init_database import db

class Question(db.Model):
    __tablename__ = 'Question'
    __table_args__ = {'extend_existing': True}
    ID_Question = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Texte = db.Column(db.String(150), nullable=False)
    Type = db.Column(db.String(50), nullable=False)
    Catégorie = db.Column(db.String(50), nullable=False)
    Faite = db.Column(db.Boolean, nullable=False)


class Formulaire(db.Model):
    __tablename__ = 'Formulaire'
    __table_args__ = {'extend_existing': True}
    ID_Formulaire = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nom_Formulaire = db.Column(db.String(50), nullable=False)
    Description_Formulaire = db.Column(db.String(250), nullable=False)


class EmissionCO2(db.Model):
    __tablename__ = 'EmissionCO2'
    __table_args__ = {'extend_existing': True}
    ID_EmissionCO2 = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Element_EmissionCO2 = db.Column(db.String(50), nullable=False)
    Coefficient_EmissionCO2 = db.Column(db.Numeric(15, 2), nullable=False)


class BilanCarbone(db.Model):
    __tablename__ = 'BilanCarbone'
    __table_args__ = {'extend_existing': True}
    ID_BilanCarbone = db.Column(db.Integer, primary_key=True, autoincrement=True)
    BilanTotal = db.Column(db.Numeric(15, 2), nullable=False)
    BilanCatégorie = db.Column(db.Numeric(15, 2), nullable=False)
    Date_BilanCarbone = db.Column(db.Date, nullable=False)
    Num_Utilisateur = db.Column(db.Integer, db.ForeignKey('Utilisateur_EFREI.Num_Utilisateur'), nullable=False)

    utilisateur = db.relationship('Utilisateur_EFREI', backref=db.backref('bilans_carbone', lazy=True))


class Répondre(db.Model):
    __tablename__ = 'Répondre'
    __table_args__ = {'extend_existing': True}
    Num_Utilisateur = db.Column(db.Integer, db.ForeignKey('Utilisateur_EFREI.Num_Utilisateur'), primary_key=True)
    ID_Question = db.Column(db.Integer, db.ForeignKey('Question.ID_Question'), primary_key=True)
    Faite = db.Column(db.Boolean, nullable=False)

    utilisateur = db.relationship('Utilisateur_EFREI', backref=db.backref('répondre', lazy=True))
    question = db.relationship('Question', backref=db.backref('répondre', lazy=True))


class Conseil(db.Model):
    __tablename__ = 'Conseil'
    __table_args__ = {'extend_existing': True}
    ID_Conseil = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Texte = db.Column(db.String(200), nullable=False)
    Catégorie = db.Column(db.String(100), nullable=False)


class Promotion(db.Model):
    __tablename__ = 'Promotion'
    __table_args__ = {'extend_existing': True}
    ID_Promotion = db.Column(db.Integer, primary_key=True)
    Année = db.Column(db.String(50), nullable=False)


class Reponse(db.Model):
    __tablename__ = 'Reponse'
    __table_args__ = {'extend_existing': True}
    ID_Reponse = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Texte_reponse = db.Column(db.String(500), nullable=False)
    Type = db.Column(db.String(50), nullable=False)
    Catégorie = db.Column(db.String(50), nullable=False)
    ID_Question = db.Column(db.Integer, db.ForeignKey('Question.ID_Question'), nullable=False)
    ID_EmissionCO2 = db.Column(db.Integer, db.ForeignKey('EmissionCO2.ID_EmissionCO2'), nullable=True)

    question = db.relationship('Question', backref=db.backref('reponses', lazy=True))
    emissionCO2 = db.relationship('EmissionCO2', backref=db.backref('reponses', lazy=True))


class Utilisateur_EFREI(db.Model):
    __tablename__ = 'Utilisateur_EFREI'
    __table_args__ = {'extend_existing': True}
    Num_Utilisateur = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nom = db.Column(db.String(50), nullable=False)
    Prénom = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(60), nullable=False, unique=True)
    MotDePasse_Utilisateur = db.Column(db.String(1000), nullable=False)
    notification_swim = db.Column(db.Boolean, default=False)
    notification_semestre = db.Column(db.Boolean, default=False)
    token_swim = db.Column(db.String(5000))
    token_semestre = db.Column(db.String(5000))
    ID_Promotion = db.Column(db.Integer, db.ForeignKey('Promotion.ID_Promotion'), nullable=False)

    promotion = db.relationship('Promotion', backref=db.backref('utilisateurs', lazy=True))


class Remplir(db.Model):
    __tablename__ = 'Remplir'
    __table_args__ = {'extend_existing': True}
    Num_Utilisateur = db.Column(db.Integer, db.ForeignKey('Utilisateur_EFREI.Num_Utilisateur'), primary_key=True)
    ID_Formulaire = db.Column(db.Integer, db.ForeignKey('Formulaire.ID_Formulaire'), primary_key=True)

    utilisateur = db.relationship('Utilisateur_EFREI', backref=db.backref('remplir', lazy=True))
    formulaire = db.relationship('Formulaire', backref=db.backref('remplir', lazy=True))


class Avoir(db.Model):
    __tablename__ = 'Avoir'
    __table_args__ = {'extend_existing': True}
    ID_Question = db.Column(db.Integer, db.ForeignKey('Question.ID_Question'), primary_key=True)
    ID_Formulaire = db.Column(db.Integer, db.ForeignKey('Formulaire.ID_Formulaire'), primary_key=True)

    question = db.relationship('Question', backref=db.backref('avoir', lazy=True))
    formulaire = db.relationship('Formulaire', backref=db.backref('avoir', lazy=True))


class Contenir(db.Model):
    __tablename__ = 'Contenir'
    __table_args__ = {'extend_existing': True}
    ID_EmissionCO2 = db.Column(db.Integer, db.ForeignKey('EmissionCO2.ID_EmissionCO2'), primary_key=True)
    ID_BilanCarbone = db.Column(db.Integer, db.ForeignKey('BilanCarbone.ID_BilanCarbone'), primary_key=True)

    emissionCO2 = db.relationship('EmissionCO2', backref=db.backref('contenir', lazy=True))
    bilanCarbone = db.relationship('BilanCarbone', backref=db.backref('contenir', lazy=True))


class Donner(db.Model):
    __tablename__ = 'Donner'
    __table_args__ = {'extend_existing': True}
    Num_Utilisateur = db.Column(db.Integer, db.ForeignKey('Utilisateur_EFREI.Num_Utilisateur'), primary_key=True)
    ID_Conseil = db.Column(db.Integer, db.ForeignKey('Conseil.ID_Conseil'), primary_key=True)

    utilisateur = db.relationship('Utilisateur_EFREI', backref=db.backref('donner', lazy=True))
    conseil = db.relationship('Conseil', backref=db.backref('donner', lazy=True))
