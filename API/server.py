from flask import Flask
from flask_cors import CORS
from Database.init_database import db

import os
from dotenv import load_dotenv

import Routes.system_routes
import Routes.user_routes
import Routes.co2_routes
import Routes.formulaire_routes

env_path = './Database/config_database.env'
load_dotenv(dotenv_path=env_path)
BDD_Name = os.getenv('BDD_Name')
Username = os.getenv('Username_')
Password = os.getenv('Password')

print(BDD_Name, Username, Password)

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{Username}:{Password}@localhost/{BDD_Name}'
app.config['SECRET_KEY'] = "my-secret-key"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

Routes.system_routes.init_system_routes(app)
Routes.user_routes.init_user_routes(app, db)
Routes.co2_routes.init_co2_routes(app, db)
Routes.formulaire_routes.init_formulaire_routes(app, db)

if __name__ == '__main__':
   app.run(port=5000)