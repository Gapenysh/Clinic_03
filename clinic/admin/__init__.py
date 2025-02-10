__all__ = ("admin_blueprint",)

from flask import Blueprint

from .doctors_routes import admin_doctors_route
from .auth_route import admin_auth_route
from .services_route import admin_services_route
from .records_route import admin_records_route
from .analysis_route import admin_analysis_route
from .actions_route import admin_actions_route
from .reviews_route import admin_reviews_route

admin_blueprint = Blueprint("admin_main", __name__)
admin_blueprint.register_blueprint(admin_doctors_route)
admin_blueprint.register_blueprint(admin_services_route)
admin_blueprint.register_blueprint(admin_auth_route)
admin_blueprint.register_blueprint(admin_records_route)
admin_blueprint.register_blueprint(admin_analysis_route)
admin_blueprint.register_blueprint(admin_actions_route)
admin_blueprint.register_blueprint(admin_reviews_route)
