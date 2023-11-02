from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# file_path = os.path.abspath(os.getcwd())+"/order/instance/test.db"
# print(file_path)



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = 'my-name-is-Moe'
# print(os.environ.get('SECRET_KEY'))

db = SQLAlchemy(app)

from order import routes