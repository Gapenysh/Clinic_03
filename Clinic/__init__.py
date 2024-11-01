__all__ = ("clinic_blueprint",)

from flask import Blueprint

from .analysis import analisys_blueprint
from .doctors import doctors_blueprint

clinic_blueprint = Blueprint("clinic", __name__)
clinic_blueprint.register_blueprint(analisys_blueprint)
clinic_blueprint.register_blueprint(doctors_blueprint)

