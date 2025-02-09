__all__ = ("appointments_blueprint",)

from flask import Blueprint

from .appointments_routes import appointments_route

appointments_blueprint = Blueprint("appointments_main", __name__)
appointments_blueprint.register_blueprint(appointments_route)
