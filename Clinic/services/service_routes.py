from flask import Blueprint, jsonify
from Clinic.bl_models.services_bl import ServiceBL

services_route = Blueprint("services_route", __name__)

@services_route.route("/services", methods=["GET"])
def get_services():
    data, error = ServiceBL.get_specialities()
    if error:
        return jsonify({"error": error}), 500

    return jsonify(data), 200

