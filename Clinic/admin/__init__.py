__all__ = ("admin_blueprint",)

from flask import Blueprint

from .doctors_routes import admin_doctors_route

admin_blueprint = Blueprint("admin_main", __name__)
admin_blueprint.register_blueprint(admin_doctors_route)
