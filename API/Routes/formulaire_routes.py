import Functions.formulaire_functions
from flask import jsonify, request
from middleware.authMiddleware import verify_token


def init_formulaire_routes(app, db):
    route_init = 0