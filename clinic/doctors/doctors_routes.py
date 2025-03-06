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


@doctors_route.route("/records/doctors", methods=["GET"])
def get_doctors_for_record():
    specialty_id = request.args.get('specialty_id')
    doctors = DoctorBL.get_doctors_for_record(specialty_id)
    return jsonify(doctors)


@doctors_route.route("/records/available-times", methods=["GET"])
def get_available_times_fo_doctor():
    id_easyclinic = request.args.get('id_easyclinic')

    available_times = DoctorBL.get_available_time_for_doctor(id_easyclinic)

    return jsonify({
        "available_times": available_times
    })



@doctors_route.route('/doctors/<int:doctor_id>', methods=["GET"])
def get_doctor(doctor_id: int):
    doctor_data = DoctorBL.get_doctor(doctor_id)
    return jsonify(doctor_data)



