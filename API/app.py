import json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_api():
    return jsonify("Hello from the API")

if __name__ == '__main__':
   app.run(port=5000)