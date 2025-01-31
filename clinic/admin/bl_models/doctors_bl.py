from flask import jsonify
from clinic.admin.dal_models.doctors_dal import DoctorDAL

class DoctorBL(object):
    @staticmethod
    def add_specialties(specialties):
        return DoctorDAL.add_specialties(specialties)


    @staticmethod
    def add_doctors(doctors):
        return DoctorDAL.add_doctors(doctors)

    @staticmethod
    def add_branches(doctors):
        return DoctorDAL.add_branches(doctors)