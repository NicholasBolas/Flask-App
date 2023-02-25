from flask import Flask
from config import Config

#app.config.from_pyfile('config.py')


app = Flask(__name__)
from app import routes

app.config.from_object(Config)
