from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta



auth_bp = Blueprint('auth', __name__, url_prefix='/api')

@auth_bp.route('/login', methods=['POST'])
def login():
    from . import jwt
    data = request.get_json()
    # Authenticating user
    if data['username'] == 'admin' and data['password'] == 'admin':
        access_token = create_access_token(identity=data['username'], expires_delta=timedelta(days=7))
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Invalid credentials"}), 401
