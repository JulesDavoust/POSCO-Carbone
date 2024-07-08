import Functions.co2_functions
from flask import jsonify, request
from middleware.authMiddleware import verify_token

# fonction qui permet de get les informations de la table utilisateur et questions
