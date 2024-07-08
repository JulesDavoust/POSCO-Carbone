from flask import Flask
from flask_cors import CORS
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from Functions.user_functions import send_notifications

from Database.init_database import db

import os
from dotenv import load_dotenv
 
import Routes.co2_routes
import Routes.formulaire_routes 
import Routes.system_routes 
import Routes.user_routes 

env_path = './Database/config_database.env'
load_dotenv(dotenv_path=env_path)
BDD_Name = os.getenv('BDD_Name')
Username = os.getenv('Username_')
Password = os.getenv('Password')
EmailUser = os.getenv('EmailUser')
EmailPass = os.getenv('EmailPassword')

print(EmailUser, EmailPass, Password)

app = Flask(__name__)
CORS(app)

# Configurer la base de données MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://root:root@localhost/posco')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = EmailUser
app.config['MAIL_PASSWORD'] = EmailPass

db.init_app(app)
mail = Mail(app)

Routes.system_routes.init_system_routes(app)
Routes.user_routes.init_user_routes(app, db, mail)
Routes.co2_routes.init_co2_routes(app, db)
Routes.formulaire_routes.init_formulaire_routes(app, db)


with app.app_context():
    db.create_all()

def send_notifications_job():
    print("job")
    send_notifications(app, db, mail)

scheduler = BackgroundScheduler()
scheduler.add_job(send_notifications_job, 'interval', minutes=5)
scheduler.start()

if __name__ == '__main__':
   app.run(port=5000)