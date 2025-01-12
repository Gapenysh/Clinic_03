from flask import Blueprint, jsonify
from clinic.bl_models.doctors_bl import DoctorBL

doctors_route = Blueprint("doctors_route", __name__)

def make_response(success: int, data=None, error_message=None, status=200):
    return jsonify({
        "success": success,
        "data": data,
        "error_message": error_message
    }), status

@doctors_route.route('/doctors', methods=['GET'])
def get_doctors():
    doctors_data, error = DoctorBL.get_all_doctors_info()
    if error:
        return make_response(success=0, error_message=error, status=500)
    return make_response(success=1, data={"doctors": doctors_data})

@doctors_route.route('/doctors/<int:doctor_id>', methods=["GET"])
def get_doctor(doctor_id: int):
    if doctor_id <= 0:
        return make_response(success=0, error_message="Invalid doctor ID provided.", status=400)

    doctor_data, error = DoctorBL.get_doctor(doctor_id)
    if error:
        return make_response(success=0, error_message=error, status=404)

    return make_response(success=1, data=doctor_data)
