from flask import Blueprint, request, jsonify
from clinic.bl_models.records_bl import RecordBL

records_route = Blueprint("records_route", __name__)

@records_route.route("/main/records", methods=["POST"])
def create_record():
    data = request.json
    success, error = RecordBL.create_record(data)
    if error:
        return jsonify({"error": error}), 500

    return jsonify({"success": success}), 200