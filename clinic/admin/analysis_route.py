from flask import Blueprint, jsonify, request
from clinic.admin.bl_models.analysis_bl import AnalyseBL

admin_analysis_route = Blueprint("admin_analysis_route", __name__)


@admin_analysis_route.route("/admin/analysis", methods=["GET"])
def get_all_analysis():
    analysis, error = AnalyseBL.get_all_analysis()

    if error:
        return jsonify({"error": error}), 500
    return analysis


@admin_analysis_route.route("/admin/categories", methods=["GET"])
def get_all_categories():
    categories, error = AnalyseBL.get_all_categories()

    if error:
        return jsonify({"error": error}), 500
    return jsonify([{"id": category[0], "name": category[1], "description": category[2]} for category in categories]), 200


@admin_analysis_route.route("/admin/categories", methods=["POST"])
def create_category():
    data = request.json
    category_id, error = AnalyseBL.create_category(data.get("name"), data.get("description"), data.get("analysis"))

    if error:
        return jsonify({"error": error}), 500
    return jsonify({"id": category_id}), 201


@admin_analysis_route.route("/admin/categories/<int:category_id>", methods=["PUT"])
def update_category(category_id):
    data = request.json
    success, error = AnalyseBL.update_category(category_id, data.get("name"), data.get("description"), data.get("analysis"))

    if error:
        return jsonify({"error": error}), 500
    return jsonify({"success": success}), 200


@admin_analysis_route.route("/admin/analysis", methods=["POST"])
def create_analysis():
    data = request.json
    analysis_id, error = AnalyseBL.create_analysis(data.get("name"), data.get("price"), data.get("category_id"))

    if error:
        return jsonify({"error": error}), 500
    return jsonify({"id": analysis_id}), 201


@admin_analysis_route.route("/admin/analysis/<int:analysis_id>", methods=["PUT"])
def update_analysis(analysis_id):
    data = request.json
    success, error = AnalyseBL.update_analysis(analysis_id, data.get("name"), data.get("price"), data.get("category_id"))
    if error:
        return jsonify({"error": error}), 500
    return jsonify({"success": success}), 200


@admin_analysis_route.route("/admin/analysis-categories", methods=["GET"])
def get_analysis_and_categories():
    data, error = AnalyseBL.get_analysis_and_categories()
    if error:
        return jsonify({"error": error}), 500
    return jsonify([{"analysis_name": row[0], "category_name": row[1]} for row in data]), 200


@admin_analysis_route.route("/admin/analysis/<int:analyse_id>", methods=["DELETE"])
def delete_analyse(analyse_id):
    success, error = AnalyseBL.delete_analyse(analyse_id)
    if error:
        return jsonify({"error": error}), 500
    return jsonify({"success": success}), 200


@admin_analysis_route.route("/admin/categories/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    success, error = AnalyseBL.delete_category(category_id)
    if error:
        return jsonify({"error": error}), 500
    return jsonify({"success": success}), 200

