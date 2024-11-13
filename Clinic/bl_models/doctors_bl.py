from flask import jsonify

from Clinic.dal_models.doctors_dal import DoctorDAL


class DoctorBL(object):
    @staticmethod
    def get_doctors():
        doctors_data, error = DoctorDAL.get_doctors()

        if error is None:
            return doctors_data, None
        else:
            return None, error

    @staticmethod
    def get_doctor(doctor_id: int):
        doctor_data, error = DoctorDAL.get_doctor(doctor_id)

        if error is None:
            return doctor_data, None
        else:
            return None, doctor_data
    @staticmethod
    def add_doctor(name: str, rating:int, edu:str, exp:int, speciality_id: int):
        success = DoctorDAL.add_doctor(name, rating, edu, exp, speciality_id)
        if not success:
            return None, {"message": "Doctor not added"}
        return success
