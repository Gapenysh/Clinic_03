__all__ = ("services_blueprint",)

from flask import Blueprint

from .service_routes import services_route

services_blueprint = Blueprint("services_main", __name__)
services_blueprint.register_blueprint(services_route)
