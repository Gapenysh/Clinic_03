from flask import Blueprint, jsonify, request
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

__all__ = ("admin_blueprint",)
admin_blueprint = Blueprint("admin_main", __name__)

from .doctors_routes import admin_doctors_route
from .auth_route import admin_auth_route
from .services_route import admin_services_route
from .records_route import admin_records_route
from .analysis_route import admin_analysis_route
from .actions_route import admin_actions_route
from .reviews_route import admin_reviews_route

admin_blueprint.register_blueprint(admin_doctors_route)
admin_blueprint.register_blueprint(admin_services_route)
admin_blueprint.register_blueprint(admin_auth_route)
admin_blueprint.register_blueprint(admin_records_route)
admin_blueprint.register_blueprint(admin_analysis_route)
admin_blueprint.register_blueprint(admin_actions_route)
admin_blueprint.register_blueprint(admin_reviews_route)


@admin_blueprint.before_request
def protect_admin_routes():
    print(f"Request endpoint: {request.endpoint}")
    if request.endpoint == "clinic.admin_main.admin_auth_route.auth_admin":
        return

    try:
        verify_jwt_in_request()
    except Exception as e:
        return jsonify({"success": 0, "message": str(e)}), 401