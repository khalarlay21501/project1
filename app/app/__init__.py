from flask import Flask
from app.routes import main
def create():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
    