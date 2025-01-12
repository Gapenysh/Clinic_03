from flask import Blueprint, jsonify, request
from clinic.admin.bl_models.doctors_bl import DoctorBL

admin_doctors_route = Blueprint("admin_doctors_route", __name__)


@admin_doctors_route.route("/admin/doctors", methods=["POST"])
def add_doctor():
    doctor_data = request.get_json()

    full_name = doctor_data.get("full_name")
    specialties_id = doctor_data.get("specialties_id")
    experience = doctor_data.get("experience")
    qualifications = doctor_data.get("qualifications")
    phone_number = doctor_data.get("phone_number")
    image = doctor_data.get("image")

    doctor_id, error = DoctorBL.add_doctor(
        full_name,
        specialties_id,
        experience,
        qualifications,
        phone_number,
        image
    )

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"Failed to add doctor: {error}"
        }), 500

    return jsonify({
        "success": 1,
        "doctor_id": doctor_id
    }), 201


@admin_doctors_route.route("/admin/doctors/<int:doctor_id>", methods=["PUT"])
def update_doctor(doctor_id):
    doctor_data = request.get_json()


    full_name = doctor_data.get("full_name")
    specialties_id = doctor_data.get("specialties_id")
    experience = doctor_data.get("experience")
    qualifications = doctor_data.get("qualifications")
    phone_number = doctor_data.get("phone_number")
    image = doctor_data.get("image")

    success, error = DoctorBL.update_doctor(
        doctor_id,
        full_name,
        specialties_id,
        experience,
        qualifications,
        phone_number,
        image
    )

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"Failed to update doctor: {error}"
        }), 500

    return jsonify({
        "success": 1,
        "doctor_id": doctor_id
    }), 200


@admin_doctors_route.route("/admin/doctors/<int:doctor_id>", methods=["DELETE"])
def delete_doctor(doctor_id):
    success, error = DoctorBL.delete_doctor(doctor_id)

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"Failed to delete doctor: {error}"
        }), 500

    return jsonify({
        "success": 1,
        "message": "Doctor deleted successfully"
    }), 200


