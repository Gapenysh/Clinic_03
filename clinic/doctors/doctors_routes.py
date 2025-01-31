from flask import Blueprint, jsonify
from clinic.bl_models.doctors_bl import DoctorBL

doctors_route = Blueprint("doctors_route", __name__)


@doctors_route.route('/doctors', methods=['GET'])
def get_doctors():
    doctors_data = DoctorBL.get_doctors()
    return jsonify(doctors_data)


@doctors_route.route('/doctors/<int:doctor_id>', methods=["GET"])
def get_doctor(doctor_id: int):
    doctor_data = DoctorBL.get_doctor(doctor_id)
    return jsonify(doctor_data)
