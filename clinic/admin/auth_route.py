from flask import Blueprint, jsonify, request
from clinic.bl_models.admin_bl import AdminBL

admin_auth_route = Blueprint("admin_auth_route", __name__)


@admin_auth_route.route("/admin/login", methods=["POST"])
def auth_admin():
    auth_json = request.get_json()

    email = auth_json.get("email")
    password = auth_json.get("password")
    if email is None or password is None:
        print("Not all data was transferred")
        return jsonify({"message": "Please enter all the fields"}), 400

    token = AdminBL.login(email, password)
    if token:
        return jsonify({"token": token}), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401