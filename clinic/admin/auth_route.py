from flask import Blueprint, jsonify, request
from clinic.bl_models.admin_bl import AdminBL
from flask_jwt_extended import get_jwt_identity, jwt_required

admin_auth_route = Blueprint("admin_auth_route", __name__)


@admin_auth_route.route("/admin/login", methods=["POST"])
def auth_admin():
    auth_json = request.get_json()

    email = auth_json.get("login")
    password = auth_json.get("password")
    if email is None or password is None:
        return jsonify({"message": "please enter all the fields"}), 400

    tokens = AdminBL.login(email, password)
    if tokens:
        access_token, refresh_token = tokens
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    else:
        return jsonify({"message": "invalid email or password"}), 401


@admin_auth_route.route("/admin/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = AdminBL.create_token(current_user)
    return jsonify(access_token=new_access_token), 200



@admin_auth_route.route("/admin/register", methods=["POST"])
def create_admin():
    admin_data = request.get_json()

    name = admin_data["name"]
    login = admin_data["login"]
    password = admin_data["password"]

    admin_id = AdminBL.register_new_admin(login, name, password)

    if admin_id:
        return jsonify({
            "admin_id": admin_id,
            "message": "new admin successfully created"
        })
    else:
        return jsonify({
            "message": "failed to create admin"
        })
