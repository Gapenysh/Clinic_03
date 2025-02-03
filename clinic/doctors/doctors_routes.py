from flask import Blueprint, jsonify, request

from clinic.bl_models.doctors_bl import DoctorBL

doctors_route = Blueprint("doctors_route", __name__)


@doctors_route.route('/doctors', methods=['GET'])
def get_doctors():
    specialty_id = request.args.get('specialty_id')
    doctors_data = DoctorBL.get_doctors(specialty_id)
    return jsonify(doctors_data)


@doctors_route.route('/main/doctors', methods=['GET'])
def get_doctors_for_main():
    doctors_data = DoctorBL.get_doctors_for_main()
    return jsonify(doctors_data)



@doctors_route.route('/doctors/<int:doctor_id>', methods=["GET"])
def get_doctor(doctor_id: int):
    doctor_data = DoctorBL.get_doctor(doctor_id)
    return jsonify(doctor_data)
