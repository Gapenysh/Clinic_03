__all__ = ("clinic_blueprint",)

from flask import Blueprint

from .analysis import analysis_blueprint
from .doctors import doctors_blueprint
from .records import records_blueprint

clinic_blueprint = Blueprint("clinic", __name__)
clinic_blueprint.register_blueprint(analysis_blueprint)
clinic_blueprint.register_blueprint(doctors_blueprint)
clinic_blueprint.register_blueprint(records_blueprint)

