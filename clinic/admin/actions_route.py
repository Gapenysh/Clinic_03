from flask import Blueprint, jsonify, request
from clinic.admin.bl_models.actions_bl import ActionBL

admin_actions_route = Blueprint("admin_actions_route", __name__)


@admin_actions_route.route("/admin/actions", methods=["POST"])
def add_actions():
    data = request.json
    actions_id, error = ActionBL.add_action(data.get("photo"), data.get("description"), data.get("category_id"))

    if error:
        return jsonify({"error": error}), 500

    return jsonify({"id": actions_id}), 201


