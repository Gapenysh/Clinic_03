from flask import Blueprint, jsonify
from clinic.bl_models.actions_bl import ActionBL

actions_route = Blueprint("actions_route", __name__)

@actions_route.route("/actions", methods=["GET"])
def get_actions():
    data, error = ActionBL.get_actions()
    if error:
        return jsonify({"error": error}), 500

    return jsonify(data), 200
