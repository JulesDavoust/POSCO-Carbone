from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurer la base de données MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:adminadmin@localhost/posco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèle de la base de données
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

# Initialiser la base de données
with app.app_context():
    db.create_all()

# Route pour ajouter un utilisateur
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user added!'}), 201

# Route pour obtenir tous les utilisateurs
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {'id': user.id, 'name': user.name, 'email': user.email}
        output.append(user_data)
    return jsonify({'users': output})

# Route pour obtenir un utilisateur par ID
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email})

# Route pour mettre à jour un utilisateur
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated!'})

# Route pour supprimer un utilisateur
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted!'})

if __name__ == '__main__':
    app.run(debug=True)
