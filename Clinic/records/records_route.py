from flask import Blueprint, jsonify, request
from Clinic.bl_models.records_bl import RecordBL

records_route = Blueprint("records_route", __name__)

@records_route.route("/add_record", methods=["POST"])
def add_record():
    data = request.get_json()

    required_fields = ["doctor_id", "service_id", "patient_name", "record_date", "record_time"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({
            "success": 0,
            "error_message": f"Missing fields: {', '.join(missing_fields)}"
        }), 400

    doctor_id = data.get("doctor_id")
    service_id = data.get("service_id")
    patient_name = data.get("patient_name")
    record_date = data.get("record_date")
    record_time = data.get("record_time")

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
        record_date,
        record_time
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
