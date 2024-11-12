from Clinic.db_connection import connection_db


class RecordDAL(object):
    @staticmethod
    def add_record(
        doctor_id: int,
        service_id: int,
        patient_name: str,
        record_date: str,
        record_time: str,
    ):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = F'''INSERT INTO record (doctor_id, service_id, patient_name, record_date, record_time, status)
                         VALUES (%s, %s, %s, %s, %s, %s) RETURNING id'''

                cursor.execute(query, (doctor_id, service_id, patient_name, record_date, record_time))
                record_id = cursor.fetchone()
                conn.commit()

                return record_id, None

        except Exception as e:
            return None, str(e)

        finally:
            conn.close()
