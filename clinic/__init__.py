__all__ = ("clinic_blueprint",)

from flask import Blueprint

from .analysis import analysis_blueprint
from .doctors import doctors_blueprint
from .records import records_blueprint
from .admin import admin_blueprint
from .services import services_blueprint
from .actions import actions_blueprint
from .appointments import appointments_blueprint

clinic_blueprint = Blueprint("clinic", __name__)
clinic_blueprint.register_blueprint(analysis_blueprint)
clinic_blueprint.register_blueprint(doctors_blueprint)
clinic_blueprint.register_blueprint(records_blueprint)
clinic_blueprint.register_blueprint(services_blueprint)
clinic_blueprint.register_blueprint(admin_blueprint)
clinic_blueprint.register_blueprint(actions_blueprint)
clinic_blueprint.register_blueprint(appointments_blueprint)
