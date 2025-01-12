from clinic.dal_models.records_dal import RecordDAL

class RecordBL(object):
    @staticmethod
    def add_record(
        doctor_id: int,
        service_id: int,
        patient_name: str,
        patient_surname: str,
        patient_phone: str,
        record_date: str,
    ):
        record_id, error = RecordDAL.add_record(
            doctor_id,
            service_id,
            patient_name,
            patient_surname,
            patient_phone,
            record_date,
        )

        if error is None:
            return record_id, None
        else:
            return None, error

    @staticmethod
    def add_bid(
        patient_surname: str,
        patient_name: str,
        patient_date_of_birth: str,
        patient_phone: str,
        speciality_id: int,
        personal_data: bool
    ):
        bid_id, error = RecordDAL.add_bid(
            patient_surname,
            patient_name,
            patient_date_of_birth,
            patient_phone,
            speciality_id,
            personal_data
        )

        if error is None:
            return bid_id, None
        else:
            return None, error
