__all__ = ("analysis_blueprint",)

from flask import Blueprint

from .analysis_routes import analysis_route

analysis_blueprint = Blueprint("analysis_main", __name__)
analysis_blueprint.register_blueprint(analysis_route)
