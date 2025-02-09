from flask import Blueprint, jsonify, request
import requests

from clinic.admin.bl_models.doctors_bl import DoctorBL
from clinic.config import settings

admin_doctors_route = Blueprint("admin_doctors_route", __name__)


@admin_doctors_route.route("/admin/branches", methods=["POST"])
def add_branches():
    api_url = f'{settings.EASYCLINIC_API_URL}/branches'
    api_key = f'Bearer {settings.EASYCLINIC_API_KEY}'
    headers = {
        "accept": "application/json",
        "Authorization": api_key
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        branches_data = response.json()
        print(branches_data)
        success = DoctorBL.add_branches(branches_data)
        if success == 1:
            return jsonify({"message": "Branches added successfully"}), 200
        else:
            return jsonify({"error": success}), 500
    else:
        return jsonify({"error": "Failed to fetch branches"}), response.status_code


@admin_doctors_route.route("/admin/specialties", methods=["POST"])
def add_specialties():
    data = request.get_json()
    filial_id = data.get('filial_id')
    api_url = f'{settings.EASYCLINIC_API_URL}/specialties'
    api_key = f'Bearer {settings.EASYCLINIC_API_KEY}'

    headers = {
        "accept": "application/json",
        "Authorization": api_key
    }

    params = {}

    if filial_id:
        params['filial_id'] = filial_id

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        specialties_data = response.json()
        success = DoctorBL.add_specialties(specialties_data)
        if success == 1:
            return jsonify({"message": "Specialties added successfully"}), 200
        else:
            return jsonify({"error": success}), 500
    else:
        return jsonify({"error": "Failed to fetch specialties"}), response.status_code



@admin_doctors_route.route("/admin/doctors", methods=["POST"])
def add_doctors():
    speciality = request.args.get('speciality')
    filial_id = request.args.get('filial_id')
    api_url = f'{settings.EASYCLINIC_API_URL}/doctors'
    api_key = f'Bearer {settings.EASYCLINIC_API_KEY}'
    headers = {
        "accept": "application/json",
        "Authorization": api_key
    }
    params = {}
    if speciality:
        params['speciality'] = speciality
    if filial_id:
        params['filial_id'] = filial_id

    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        doctors_data = response.json()
        success = DoctorBL.add_doctors(doctors_data)
        if success == 1:
            return jsonify({"message": "Doctors added successfully"}), 200
        else:
            return jsonify({"error": success}), 500
    else:
        return jsonify({"error": "Failed to fetch doctors"}), response.status_code


@admin_doctors_route.route("/admin/doctors", methods=["GET"])
def get_doctors():
    doctors_data = DoctorBL.get_doctors()

    return doctors_data


@admin_doctors_route.route("/admin/doctors/<int:doctor_id>", methods=["PUT"])
def edit_doctors(doctor_id):
    data = request.get_json()
    success = DoctorBL.edit_doctor(doctor_id, data)
    if success == 1:
        return jsonify({"message": "Doctor updated successfully"}), 200
    else:
        return jsonify({"error": success}), 500