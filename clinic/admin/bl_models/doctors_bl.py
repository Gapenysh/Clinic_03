from flask import jsonify
from clinic.admin.dal_models.doctors_dal import DoctorDAL

class DoctorBL(object):
    @staticmethod
    def add_doctor(
            full_name: str,
            specialties_id: list,
            experience: int,
            qualifications: list,
            phone_number: str,
            image: str
    ):

        doctor_id, error = DoctorDAL.add_doctor(
            full_name,
            specialties_id,
            experience,
            qualifications,
            phone_number,
            image
        )

        if error is None:
            return doctor_id, None

        else:
            return None, error

    @staticmethod
    def update_doctor(
            doctor_id: int,
            full_name: str,
            specialties_id: list,
            experience: int,
            qualifications: list,
            phone_number: str,
            image: str
    ):
        success, error = DoctorDAL.update_doctor(
            doctor_id,
            full_name,
            specialties_id,
            experience,
            qualifications,
            phone_number,
            image
        )

        if error is None:
            return True, None
        else:
            return False, error

    @staticmethod
    def delete_doctor(doctor_id: int):
        success, error = DoctorDAL.delete_doctor(doctor_id)

        if error is None:
            return True, None
        else:
            return False, error