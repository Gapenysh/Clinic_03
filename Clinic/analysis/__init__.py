__all__ = ("analisys_blueprint",)

from flask import Blueprint

from .analysis_routes import analisys_route

analisys_blueprint = Blueprint("analisys_main", __name__)
analisys_blueprint.register_blueprint(analisys_route)
