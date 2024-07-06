import Functions.formulaire_functions
from flask import jsonify, request
from middleware.authMiddleware import verify_token


@app.route('/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    return jsonify([question.to_dict() for question in questions])

@app.route('/question/<int:id>', methods=['GET'])
def get_question(id):
    question = Question.query.get_or_404(id)
    return jsonify(question.to_dict())

@app.route('/question', methods=['POST'])
def create_question():
    data = request.json
    new_question = Question(
        Texte=data['Texte'],
        Type=data['Type'],
        Categorie=data['Categorie'],
        Faite=data['Faite']
    )
    db.session.add(new_question)
    db.session.commit()
    return jsonify(new_question.to_dict()), 201

@app.route('/question/<int:id>', methods=['PUT'])
def update_question(id):
    question = Question.query.get_or_404(id)
    data = request.json
    question.Texte = data['Texte']
    question.Type = data['Type']
    question.Categorie = data['Categorie']
    question.Faite = data['Faite']
    db.session.commit()
    return jsonify(question.to_dict())

@app.route('/question/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = Question.query.get_or_404(id)
    db.session.delete(question)
    db.session.commit()
    return '', 204
