from flask import Blueprint, jsonify, request
import requests

from clinic.admin.bl_models.doctors_bl import DoctorBL
from clinic.config import settings

admin_doctors_route = Blueprint("admin_doctors_route", __name__)


@admin_doctors_route.route("/admin/branches", methods=["GET"])
def get_branches():
    api_url = f'{settings.EASYCLINIC_API_URL}/branches'
    api_key = f'Bearer {settings.EASYCLINIC_API_KEY}'
    headers = {
        "accept": "application/json",
        "Authorization": api_key
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch branches"}), response.status_code


@admin_doctors_route.route("/admin/specialties", methods=["POST"])
def get_specialties():
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



@admin_doctors_route.route("/admin/doctors", methods=["GET"])
def get_doctors():
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
        print(doctors_data)
        success = DoctorBL.add_doctors(doctors_data)
        if success == 1:
            return jsonify({"message": "Doctors added successfully"}), 200
        else:
            return jsonify({"error": success}), 500
    else:
        return jsonify({"error": "Failed to fetch doctors"}), response.status_code