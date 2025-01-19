from flask import Blueprint, jsonify, request
from clinic.admin.bl_models.services_bl import ServiceBL

admin_services_route = Blueprint("admin_services_route", __name__)




@admin_services_route.route("/admin/services", methods=["POST"])
def add_service():
    service_data = request.get_json()

    service_name = service_data.get("service_name")
    price = service_data.get("price")
    speciality_id = service_data.get("speciality_id")

    service_id, error = ServiceBL.add_service(service_name, price, speciality_id)

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"Не удалось добавить услугу: {error}"
        }), 500

    return jsonify({
        "success": 1,
        "service_id": service_id
    }), 201

@admin_services_route.route("/admin/services/<int:service_id>", methods=["PUT"])
def update_service(service_id):
    service_data = request.get_json()

    service_name = service_data.get("service_name")
    price = service_data.get("price")
    speciality_id = service_data.get("speciality_id")

    success, error = ServiceBL.update_service(service_id, service_name, price, speciality_id)

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"Не удалось обновить услугу: {error}"
        }), 500

    return jsonify({
        "success": 1,
        "service_id": service_id
    }), 200

@admin_services_route.route("/admin/services/<int:service_id>", methods=["DELETE"])
def delete_service(service_id):
    success, error = ServiceBL.delete_service(service_id)

    if error:
        return jsonify({
            "success": 0,
            "error_message": f"Не удалось удалить услугу: {error}"
        }), 500

    return jsonify({
        "success": 1,
        "message": "Услуга успешно удалена"
    }), 200
