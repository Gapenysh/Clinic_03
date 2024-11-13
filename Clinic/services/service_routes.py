from flask import Blueprint, jsonify, request
from Clinic.bl_models.service_bl import ServiceBL

services_route = Blueprint("services_route", __name__)


@services_route.route("/services", methods=["GET"])
def get_services_by_speciality_id():
    specialities = ServiceBL.get_specialities()

    speciality_id = request.args.get("spec_id", None)

    services = ServiceBL.get_services(speciality_id)

    return jsonify({"Specialities": f"{specialities}"},
                   {"Services": f"{services}"},)
