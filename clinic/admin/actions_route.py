from flask import Blueprint, jsonify, request
from socks import method

from clinic.admin.bl_models.actions_bl import ActionBL

admin_actions_route = Blueprint("admin_actions_route", __name__)


@admin_actions_route.route("/admin/actions", methods=["POST"])
def add_actions():
    data = request.json
    actions_id, error = ActionBL.add_action(data.get("photo"), data.get("description"), data.get("category_id"))

    if error:
        return jsonify({"error": error}), 500

    return jsonify({"id": actions_id}), 201



@admin_actions_route.route("/admin/actions", methods=["GET"])
def get_actions():
    actions, error = ActionBL.get_action()

    if error:
        return jsonify({"error": error}), 500

    return actions, 201


@admin_actions_route.route("/admin/actions/<int:action_id>", methods=["DELETE"])
def delete_actions(action_id: int):
    success, error = ActionBL.delete_action(action_id)

    if error:
        return jsonify({"error": error}), 500

    return jsonify({"success": success}), 200


@admin_actions_route.route("/admin/actions_categories", methods=["GET"])
def get_categories():
    categories_data, error = ActionBL.get_categories()

    if error:
        return jsonify({"categories_data": categories_data,"error": error}), 500

    return jsonify({"categories_data": categories_data}), 200
