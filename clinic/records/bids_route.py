from flask import Blueprint, jsonify, request

from clinic.bl_models.records_bl import RecordBL

bids_route = Blueprint("bids_route", __name__)


@bids_route.route("/bids", methods=["POST"])
def add_bid():
    bid_data = request.get_json()

    patient_surname = bid_data.get("patient_surname")
    patient_name = bid_data.get("patient_name")
    patient_date_of_birth = bid_data.get("patient_date_of_birth")
    patient_phone = bid_data.get("patient_phone")
    speciality_id = bid_data.get("speciality_id")
    personal_data = bid_data.get("personal_data")

    if not personal_data:
        return jsonify({
            "success": 0,
            "error_message": "Give your consent to the processing of personal data"
        }), 422

    if speciality_id <= 0:
        return jsonify({
            "success": 0,
            "error_message": "Invalid speciality ID provided."
        }), 400

    bid_id, error = RecordBL.add_bid(
        patient_surname,
        patient_name,
        patient_date_of_birth,
        patient_phone,
        speciality_id,
        personal_data
    )

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"Failed to add bid: {error}"
        }), 500

    return jsonify({
        "success": 1,
        "bid_id": bid_id
    }), 201