from flask import Blueprint, request, jsonify
from app.services.auth_service import authenticate
from app.utils.helpers import Helpers
from app.database.database_handler import DatabaseHandler

auth_bp = Blueprint('auth_routes', __name__)

db_handler = DatabaseHandler()
helpers = Helpers(db_handler)

@auth_bp.route('/', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify(message="Username and password are required"), 400
    
    success, access_token = authenticate(username, password, helpers)

    if success:
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message="Invalid credentials"), 401