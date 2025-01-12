from flask import Blueprint, jsonify, request
from clinic.admin.bl_models.records_bl import RecordBL

admin_records_route = Blueprint("admin_records_route", __name__)

@admin_records_route.route("/admin/records", methods=["GET"])
def get_records():
    records, error = RecordBL.get_records()

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"Не удалось получить записи: {error}"
        }), 500

    return jsonify({
        "success": 1,
        "records": records
    }), 200

@admin_records_route.route("/admin/records", methods=["POST"])
def add_record():
    record_data = request.get_json()

    patient_name = record_data.get("patient_name")
    patient_surname = record_data.get("patient_surname")
    phone_number = record_data.get("phone_number")
    appointment_date = record_data.get("appointment_date")
    doctor_id = record_data.get("doctor_id")
    service_id = record_data.get("service_id")

    record_id, error = RecordBL.add_record(patient_name, patient_surname, phone_number, appointment_date, doctor_id, service_id)

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"Не удалось добавить запись: {error}"
        }), 500

    return jsonify({
        "success": 1,
        "record_id": record_id
    }), 201

@admin_records_route.route("/admin/records/<int:record_id>", methods=["PUT"])
def update_record(record_id):
    record_data = request.get_json()

    patient_name = record_data.get("patient_name")
    patient_surname = record_data.get("patient_surname")
    phone_number = record_data.get("phone_number")
    appointment_date = record_data.get("appointment_date")
    doctor_id = record_data.get("doctor_id")
    service_id = record_data.get("service_id")

    success, error = RecordBL.update_record(record_id, patient_name, patient_surname, phone_number, appointment_date, doctor_id, service_id)

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"Не удалось обновить запись: {error}"
        }), 500

    return jsonify({
        "success": 1,
        "record_id": record_id
    }), 200

@admin_records_route.route("/admin/records/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    success, error = RecordBL.delete_record(record_id)

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"Не удалось удалить запись: {error}"
        }), 500

    return jsonify({
        "success": 1,
        "message": "Запись успешно удалена"
    }), 200
