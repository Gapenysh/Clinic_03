from flask import Blueprint, jsonify
from clinic.bl_models.analysis_bl import AnalyseBL

analysis_route = Blueprint("analysis_route", __name__)

@analysis_route.route("/analysis", methods=["GET"])
def get_analysis():
    data, error = AnalyseBL.get_analysis()
    if error:
        return jsonify({"error": error}), 500

    return jsonify(data), 200
