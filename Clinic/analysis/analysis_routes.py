from flask import Blueprint, request

from Clinic.bl_models.analysis_bl import AnalyseBL
analysis_route = Blueprint("analysis_route", __name__)

@analysis_route.route("/analysis", methods=['POST'])
def add_analysis():
    data = request.get_json()

    name = data.get("name")
    price = data.get("price")

    analyse_id, error = AnalyseBL.add_analyse(name, price, check_up)