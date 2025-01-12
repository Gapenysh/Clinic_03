from clinic.admin.dal_models.records_dal import RecordDAL

class RecordBL(object):
    @staticmethod
    def get_records():
        records, error = RecordDAL.get_records()

        if error is None:
            return records, None
        else:
            return None, error

    @staticmethod
    def add_record(patient_name: str, patient_surname: str, phone_number: str, appointment_date: str, doctor_id: int, service_id: int):
        record_id, error = RecordDAL.add_record(patient_name, patient_surname, phone_number, appointment_date, doctor_id, service_id)

        if error is None:
            return record_id, None
        else:
            return None, error

    @staticmethod
    def update_record(record_id: int, patient_name: str, patient_surname: str, phone_number: str, appointment_date: str, doctor_id: int, service_id: int):
        success, error = RecordDAL.update_record(record_id, patient_name, patient_surname, phone_number, appointment_date, doctor_id, service_id)

        if error is None:
            return True, None
        else:
            return False, error

    @staticmethod
    def delete_record(record_id: int):
        success, error = RecordDAL.delete_record(record_id)

        if error is None:
            return True, None
        else:
            return False, error
