from flask import Blueprint, jsonify, request
from Clinic.bl_models.records_bl import RecordBL

records_route = Blueprint("records_route", __name__)

@records_route.route("/records", methods=["POST"])
def add_record():
    record_data = request.get_json()

    doctor_id = record_data.get("doctor_id")
    service_id = record_data.get("service_id")
    patient_name = record_data.get("patient_name")
    patient_surname = record_data.get("patient_surname")
    patient_phone = record_data.get("patient_phone")
    record_date = record_data.get("record_date")

    if doctor_id <= 0:
        return jsonify({
            "success": 0,
            "error_message": "Invalid doctor ID provided."
        }), 400

    if service_id <= 0:
        return jsonify({
            "success": 0,
            "error_message": "Invalid service ID provided."
        }), 400

    record_id, error = RecordBL.add_record(
        doctor_id,
        service_id,
        patient_name,
        patient_surname,
        patient_phone,
        record_date,
    )

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"Failed to add record: {error}"
        }), 500

    return jsonify({
        "success": 1,
        "record_id": record_id
    }), 201
