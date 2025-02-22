import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from app.routes.admin.admin_routes import admin_bp
from app.routes.auth.auth_routes import auth_bp


def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.secret_key = os.getenv("FLASK_SECRET_KEY")

    CORS(app)

    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/')

    return app
