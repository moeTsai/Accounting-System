from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bill.db'
app.secret_key = 'my-name-is-Moe'
# print(os.environ.get('SECRET_KEY'))

db = SQLAlchemy(app)

from order import routes