__all__ = ("records_blueprint",)

from flask import Blueprint

from .records_route import records_route
from .bids_route import bids_route

records_blueprint = Blueprint("records_main", __name__)
records_blueprint.register_blueprint(records_route)
records_blueprint.register_blueprint(bids_route)