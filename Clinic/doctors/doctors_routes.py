from flask import Blueprint, jsonify

from Clinic.bl_models.doctors_bl import DoctorBL

doctors_route = Blueprint("doctors_route", __name__)


@doctors_route.route('/doctors', methods='GET')
def get_doctors():
    doctors_data, error = DoctorBL.get_doctors()

    if error is None:
        return jsonify({
            "success": 1,
            "doctors_data": doctors_data
        })
    else:
        return jsonify({
            "success": 0,
            "error_message": error
        })

@doctors_route.route('/doctors/<int:id>')
def get_doctor(doctor_id: int):
    if doctor_id <= 0:
        return jsonify({
            "success": 0,
            "error_message": "Invalid doctor ID provided."
        }), 400

    doctor_data, error = DoctorBL.get_doctor(doctor_id)

    if error is not None:
        return jsonify({
            "success": 0,
            "error_message": error
        }), 404

    return jsonify({
        "success": 1,
        "doctor_data": doctor_data
    })





