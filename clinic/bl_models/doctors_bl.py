import requests

from clinic.dal_models.doctors_dal import DoctorDAL
from clinic.config import settings


class DoctorBL(object):
    @staticmethod
    def get_available_time_for_doctor(doctor_id_easyclinic: int):
        api_url = f"{settings.EASYCLINIC_API_URL}/available-times"
        api_key = f"Bearer {settings.EASYCLINIC_API_KEY}"

        headers = {
            "accept": "application/json",
            "Authorization": api_key
        }

        params = {
            "doctor_id": doctor_id_easyclinic,
            "months": 1
        }

        response = requests.get(api_url, headers=headers, params=params)
        available_times_data = response.json()

        if "doctors" in available_times_data and available_times_data["doctors"]:
            return available_times_data["doctors"][0].get("day", [])
        else:
            return []

    @staticmethod
    def get_doctors(specialty_id=None):
        if specialty_id:
            doctors = DoctorDAL.get_doctors_by_specialty(specialty_id)
        else:
            doctors = DoctorDAL.get_doctors()

        specialties = DoctorDAL.get_specialties()
        filials = DoctorDAL.get_filials()
        reviews = DoctorDAL.get_reviews()

        for doctor in doctors:
            doctor['specialties'] = [spec for spec in specialties if int(spec['doctor_id']) == int(doctor['id'])]
            doctor['filials'] = [fil for fil in filials if int(fil['doctor_id']) == int(doctor['id'])]
            doctor['reviews'] = [rev for rev in reviews if int(rev['doctor_id']) == int(doctor['id'])]

        return doctors

    @staticmethod
    def get_doctor(doctor_id: int):

        doctor_data = DoctorDAL.get_doctor(doctor_id)

        doctor_data['available-times'] = DoctorBL.get_available_time_for_doctor(doctor_data['id_easyclinic'])

        reviews = DoctorDAL.get_reviews_by_doctor(doctor_id)
        doctor_data['reviews'] = reviews

        return doctor_data

    @staticmethod
    def get_doctors_for_main():
        return DoctorDAL.get_doctors_for_main()

    @staticmethod
    def get_doctors_for_record(specialty_id=None):
        doctors = DoctorDAL.get_doctors_for_record(specialty_id)
        return doctors