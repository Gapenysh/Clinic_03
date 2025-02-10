from flask import jsonify
from clinic.admin.dal_models.doctors_dal import DoctorDAL

class DoctorBL(object):
    @staticmethod
    def add_specialties(specialties):
        return DoctorDAL.add_specialties(specialties)


    @staticmethod
    def get_reviews():
        return DoctorDAL.get_reviews()


    @staticmethod
    def add_doctors(doctors):
        return DoctorDAL.add_doctors(doctors)


    @staticmethod
    def add_branches(doctors):
        return DoctorDAL.add_branches(doctors)


    @staticmethod
    def get_doctors():
        return DoctorDAL.get_doctors()


    @staticmethod
    def edit_doctor(doctor_id: int, data: dict):
        return DoctorDAL.edit_doctor(doctor_id, data)