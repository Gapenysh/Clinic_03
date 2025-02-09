import requests
import logging
from clinic.config import settings

class AppointmentBL(object):
    @staticmethod
    def create_appointment(data):
        api_url = f'{settings.EASYCLINIC_API_URL}/appointments'
        api_key = f'Bearer {settings.EASYCLINIC_API_KEY}'
        print(f'FULL URL - {api_url}')

        headers = {
            "accept": "application/json",
            "Authorization": api_key,
            "Content-Type": "application/json"
        }

        params = {
            "fio": data.get("fio"),
            "mobile": data.get("mobile"),
            "time": data.get("time"),
            "day_id": data.get("day_id")
        }

        logging.info(f"Sending request to {api_url} with data: {params}")

        response = requests.post(api_url, headers=headers, json=params)

        if response.status_code == 200:
            answer = response.json()
            return answer, None
        else:
            logging.error(f"Error response: {response.status_code} - {response.text}")
            return None, response.text

    @staticmethod
    def confirm_appointment(data):
        api_url = f'{settings.EASYCLINIC_API_URL}/appointments/confirm'
        api_key = f'Bearer {settings.EASYCLINIC_API_KEY}'
        print(f'FULL URL - {api_url}')

        headers = {
            "accept": "application/json",
            "Authorization": api_key,
            "Content-Type": "application/json"
        }

        params = {
            "code": data.get("code"),
            "mobile": data.get("mobile")
        }

        logging.info(f"Sending confirmation request to {api_url} with data: {params}")

        response = requests.post(api_url, headers=headers, json=params)

        if response.status_code == 200:
            confirmation = response.json()
            return confirmation, None
        else:
            logging.error(f"Error response: {response.status_code} - {response.text}")
            return None, response.text