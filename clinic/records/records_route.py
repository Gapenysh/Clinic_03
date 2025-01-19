from flask import Blueprint, jsonify, request
import requests
import logging

from clinic.config import settings

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

records_route = Blueprint("records_route", __name__)

@records_route.route('/branches', methods=['GET'])
def get_branches():
    try:
        api_url = settings.EASYCLINIC_API_URL
        api_key = settings.EASYCLINIC_API_KEY

        full_url = f'{api_url}/branches'

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        response = requests.get(full_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data), 200
        else:
            return jsonify({"error": "Failed to fetch branches"}), response.status_code

    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500


@records_route.route("/specialties", methods=["GET"])
def get_specialties():
    try:
        api_url = settings.EASYCLINIC_API_URL
        api_key = settings.EASYCLINIC_API_KEY

        full_url = f'{api_url}/specialties'

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        response = requests.get(full_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data), 200
        else:
            return jsonify({"error": "Failed to fetch specialties"}), response.status_code

    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500


@records_route.route("/records/doctors", methods=["GET"])
def get_doctors():
    try:
        doctors_data = request.get_json()
        speciality = doctors_data.get("speciality")
        filial_id = doctors_data.get("filial_id")

        logging.info(f"SPECIALITY: {speciality}\nFILIAL_ID: {str(filial_id)}")

        api_url = settings.EASYCLINIC_API_URL
        api_key = settings.EASYCLINIC_API_KEY

        full_url = f'{api_url}/doctors'

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json"
        }
        params = {
            "speciality": speciality,
            "filial_id": filial_id
        }

        response = requests.get(full_url, headers=headers, params=params)

        if response.status_code == 200:
            try:
                data = response.json()
                return jsonify(data), 200
            except ValueError:
                return jsonify({"error": "Invalid JSON in response"}), 500
        else:
            return jsonify({"error": "Failed to fetch doctors"}), response.status_code

    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@records_route.route("/records/doctors/available-times", methods=["GET"])
def get_available_slots():
    try:
        doctors_data = request.get_json()
        speciality = doctors_data.get("speciality")
        filial_id = doctors_data.get("filial_id")
        doctor_id = doctors_data.get("doctor_id")
        services = doctors_data.get("services")
        months = doctors_data.get("months")


        api_url = settings.EASYCLINIC_API_URL
        api_key = settings.EASYCLINIC_API_KEY

        full_url = f'{api_url}/available-times'

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json"
        }
        logging.info(f"headers - {headers}")


        params = {
            "doctor_id": doctor_id,
            "filial_id": filial_id,
            "speciality": speciality,
            "services": services,
            "months": months
        }
        logging.info(f"params - {params}")


        response = requests.get(full_url, headers=headers, params=params)

        if response.status_code == 200:
            try:
                data = response.json()
                logging.info(f"RESPONSE DATA - {data}")
                return jsonify(data), 200
            except ValueError:
                return jsonify({"error": "Invalid JSON in response"}), 500
        else:
            return jsonify({"error": "Failed to fetch doctors"}), response.status_code

    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500


@records_route.route("/records/appointment", methods=["POST"])
def create_appointment():
    try:
        appointment_data = request.get_json()
        speciality = appointment_data.get("speciality")
        filial_id = appointment_data.get("filial_id")
        doctor_id = appointment_data.get("doctor_id")
        date = appointment_data.get("date")
        time = appointment_data.get("time")
        mobile = appointment_data.get("mobile")
        cart = appointment_data.get("cart")



        logging.info(f"Creating appointment with data: {appointment_data}")

        api_url = settings.EASYCLINIC_API_URL
        api_key = settings.EASYCLINIC_API_KEY

        full_url = f'{api_url}/appointments/confirm'
        logging.info(f"FULL URL - {full_url}")

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json"
        }
        logging.info(f"HEADERS - {headers}")


        params = {
            "mobile": mobile,
            "cart": cart,
            "renew": True
        }
        logging.info(f"PARAMS - {params}")


        response = requests.post(full_url, headers=headers, json=params)
        logging.info(f"RESPONSE - {response}")


        if response.status_code == 200:
            try:
                data = response.json()
                logging.info(f"DATA - {data}")
                return jsonify(data), 200
            except ValueError:
                return jsonify({"error": "Invalid JSON in response"}), 500
        else:
            return jsonify({"error": "Failed to create appointment"}), response.status_code

    except requests.RequestException as e:
        logging.error(f"Error creating appointment: {str(e)}")
        return jsonify({"error": str(e)}), 500

