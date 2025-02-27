import requests

from clinic.dal_models.doctors_dal import DoctorDAL
from clinic.config import settings


class DoctorBL(object):
    @staticmethod
    def get_doctors(specialty_id=None):
        if specialty_id:
            doctors = DoctorDAL.get_doctors_by_specialty(specialty_id)
        else:
            doctors = DoctorDAL.get_doctors()

        specialties = DoctorDAL.get_specialties()
        filials = DoctorDAL.get_filials()

        api_url = f'{settings.EASYCLINIC_API_URL}/available-times'
        api_key = f'Bearer {settings.EASYCLINIC_API_KEY}'
        headers = {
            "accept": "application/json",
            "Authorization": api_key
        }

        filtered_doctors = []

        for doctor in doctors:
            params = {
                "doctor_id": 1,
                "months": 1
            }

            response = requests.get(api_url, headers=headers, params=params)
            doctor_available_times = response.json()

            doctor['specialties'] = [spec for spec in specialties if int(spec['doctor_id']) == int(doctor['id'])]
            doctor['filials'] = [fil for fil in filials if int(fil['doctor_id']) == int(doctor['id'])]
            doctor['available_times'] = doctor_available_times["doctors"][0]["day"]

            filtered_doctors.append(doctor)

        return filtered_doctors

    @staticmethod
    def get_doctor(doctor_id: int):

        doctor_data = DoctorDAL.get_doctor(doctor_id)

        api_url = f'{settings.EASYCLINIC_API_URL}/available-times'
        api_key = f'Bearer {settings.EASYCLINIC_API_KEY}'

        headers = {
            "accept": "application/json",
            "Authorization": api_key
        }

        params = {
            "doctor_id": doctor_data['id_easyclinic'],
            "months": 1
        }

        response = requests.get(api_url, headers=headers, params=params)
        doctor_available_times = response.json()

        doctor_data['available-times'] = doctor_available_times["doctors"][0]["day"]


        return doctor_data

    @staticmethod
    def get_doctors_for_main():
        return DoctorDAL.get_doctors_for_main()