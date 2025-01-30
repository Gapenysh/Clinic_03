__all__ = ("actions_blueprint",)

from flask import Blueprint

from .action_route import actions_route

actions_blueprint = Blueprint("actions_blueprint", __name__)
actions_blueprint.register_blueprint(actions_route)
