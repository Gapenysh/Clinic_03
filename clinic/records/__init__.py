__all__ = ("records_blueprint",)

from flask import Blueprint

from .records_routes import records_route

records_blueprint = Blueprint("records_main", __name__)
records_blueprint.register_blueprint(records_route)