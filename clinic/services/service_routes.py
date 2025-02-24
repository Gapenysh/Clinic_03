from flask import Blueprint, jsonify
from clinic.bl_models.services_bl import ServiceBL

services_route = Blueprint("services_route", __name__)

@services_route.route("/services", methods=["GET"])
def get_services():
    data, error = ServiceBL.get_specialities()
    if error:
        return jsonify({"error": error}), 500

    return jsonify(data), 200


@services_route.route("/specialties", methods=["GET"])
def get_specialties():
    specialties_data, error = ServiceBL.get_specialties()

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"{error}"
        }), 500

    return jsonify(specialties_data), 200