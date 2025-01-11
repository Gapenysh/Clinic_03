from flask import jsonify
from Clinic.dal_models.doctors_dal import DoctorDAL

class DoctorBL(object):
    @staticmethod
    def get_doctors():
        doctors_data, error = DoctorDAL.get_doctors()
        if error is not None:
            return None, error
        return doctors_data, None

    @staticmethod
    def get_doctor(doctor_id: int):
        doctor_data, error = DoctorDAL.get_doctor(doctor_id)
        if error is not None:
            return None, 'failed to doctors data'

        slots_data, error = DoctorDAL.get_available_slots(doctor_id)
        if error is not None:
            return None, 'failed to slots data'

        qualification_data, error = DoctorDAL.get_qualification(doctor_id)
        if error is not None:
            return None, 'failed to qualifications data'

        reviews_data, error = DoctorDAL.get_reviews(doctor_id)
        if error is not None:
            return None, 'failed to reviews data'

        for slot in slots_data:
            slot['slot_time'] = slot['slot_time'].strftime('%H:%M:%S')

        specialties_data, error = DoctorDAL.get_specialties(doctor_id)
        if error is not None:
            return None, 'failed to specialties data'

        return {"doctor": doctor_data, "available_slots": slots_data, "qualification": qualification_data,
                "reviews": reviews_data, "specialties": specialties_data}, None

    @staticmethod
    def get_all_doctors_info():
        doctors_data, error = DoctorDAL.get_doctors()
        if error is not None:
            return None, error

        all_doctors_info = []

        for doctor in doctors_data:
            doctor_id = doctor[0]  # Предполагаем, что первый элемент - это id врача
            doctor_info, error = DoctorBL.get_doctor(doctor_id)
            if error is not None:
                return None, error
            all_doctors_info.append(doctor_info)

        return all_doctors_info, None

    @staticmethod
    def add_doctor(name: str, rating: int, edu: str, exp: int, speciality_id: int):
        success = DoctorDAL.add_doctor(name, rating, edu, exp, speciality_id)
        if not success:
            return None, {"message": "Doctor not added"}
        return success, None
