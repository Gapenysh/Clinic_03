from flask import Blueprint, request, jsonify
from clinic.bl_models.appointments_bl import AppointmentBL

appointments_route = Blueprint("appointments_route", __name__)

@appointments_route.route("/appointments", methods=["POST"])
def create_appointment():
    data = request.get_json()
    print(f'appointments data - {data}')
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    success, error = AppointmentBL.create_appointment(data)
    if error:
        return jsonify({"error": error}), 500

    return jsonify({"success": success}), 200


@appointments_route.route("/appointments/confirm", methods=["POST"])
def confirm_appointment():
    data = request.get_json()
    print(f'confirm data - {data}')
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    confirmation, error = AppointmentBL.confirm_appointment(data)
    if error:
        return jsonify({"error": error}), 500

    return jsonify({"confirmation": confirmation}), 200
