__all__ = ("doctors_blueprint",)

from flask import Blueprint

from .doctors_routes import doctors_route

doctors_blueprint = Blueprint("doctors_main", __name__)
doctors_blueprint.register_blueprint(doctors_route)
