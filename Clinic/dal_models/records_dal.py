from Clinic.db_connection import connection_db


class RecordDAL(object):
    @staticmethod
    def add_record(
        doctor_id: int,
        service_id: int,
        patient_name: str,
        patient_surname: str,
        patient_phone: str,
        record_date: str,
    ):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = F'''INSERT INTO records (service_id, doctor_id, patient_name, patient_surname, phone_number, appointment_date)
                         VALUES (%s, %s, %s, %s, %s, %s) RETURNING id'''

                cursor.execute(query, (doctor_id, service_id, patient_name, patient_surname, patient_phone, record_date))
                record_id = cursor.fetchone()
                conn.commit()

                return record_id, None

        except Exception as e:
            return None, str(e)

        finally:
            conn.close()

    @staticmethod
    def add_bid(
            patient_surname: str,
            patient_name: str,
            patient_date_of_birth: str,
            patient_phone: str,
            speciality_id: int,
            personal_data: bool
    ):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = '''INSERT INTO bids (patient_surname, patient_name, patient_phone, speciality_id, personal_data, patient_date_of_birth)
                           VALUES (%s, %s, %s, %s, %s, %s)
                           RETURNING id'''

                cursor.execute(query, (
                patient_surname, patient_name, patient_phone, speciality_id, personal_data, patient_date_of_birth))
                bid_id = cursor.fetchone()
                conn.commit()

                if bid_id:
                    return bid_id[0], None
                else:
                    return None, "Failed to add bid: no results to fetch"

        except Exception as e:
            print(str(e))
            return None, str(e)

        finally:
            conn.close()


