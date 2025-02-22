from flask import Blueprint, request, jsonify
from app.services.admin_service import AdminService

admin_bp = Blueprint('admin_routes', __name__)


admin_service = AdminService()


@admin_bp.route('/users', methods=['GET'])
def get_users():
    users = admin_service.get_all_users()
    return jsonify(users), 200

