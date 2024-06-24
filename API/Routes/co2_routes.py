import Functions.co2_functions
from flask import jsonify, request
from middleware.authMiddleware import verify_token

def init_co2_routes(app, db):
    route_init = 0