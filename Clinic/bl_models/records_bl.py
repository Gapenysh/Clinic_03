from Clinic.dal_models.records_dal import RecordDAL

class RecordBL(object):
    @staticmethod
    def add_record(
        doctor_id: int,
        service_id: int,
        patient_name: str,
        record_date: str,
        record_time: str,
    ):
        record_id, error = RecordDAL.add_record(
            doctor_id,
            service_id,
            patient_name,
            record_date,
            record_time,
        )

        if error is None:
            return record_id, None
        else:
            return None, error