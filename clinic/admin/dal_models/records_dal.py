from psycopg2 import Error
from clinic.db_connection import connection_db

class RecordDAL(object):
    @staticmethod
    def get_records():
        conn = connection_db()
        records = []

        try:
            with conn.cursor() as cursor:
                query = '''SELECT id, patient_name, patient_surname, phone_number, appointment_date, doctor_id, service_id FROM records'''
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    record = {
                        "id": row[0],
                        "patient_name": row[1],
                        "patient_surname": row[2],
                        "phone_number": row[3],
                        "appointment_date": row[4],
                        "doctor_id": row[5],
                        "service_id": row[6]
                    }
                    records.append(record)
                conn.commit()

        except Exception as e:
            print(f"Ошибка при получении записей: {str(e)}")
            return None, str(e)

        finally:
            conn.close()

        return records, None

    @staticmethod
    def add_record(patient_name: str, patient_surname: str, phone_number: str, appointment_date: str, doctor_id: int, service_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = '''INSERT INTO records (patient_name, patient_surname, phone_number, appointment_date, doctor_id, service_id)
                           VALUES (%s, %s, %s, %s, %s, %s) RETURNING id'''
                cursor.execute(query, (patient_name, patient_surname, phone_number, appointment_date, doctor_id, service_id))
                result = cursor.fetchone()
                if result is not None:
                    record_id = result[0]
                    conn.commit()
                    return record_id, None
                else:
                    return None, "Не удалось добавить запись: результат запроса пуст"

        except Exception as e:
            print(f"Ошибка при добавлении записи: {str(e)}")
            return None, str(e)

        finally:
            conn.close()

    @staticmethod
    def update_record(record_id: int, patient_name: str, patient_surname: str, phone_number: str, appointment_date: str, doctor_id: int, service_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = '''UPDATE records
                           SET patient_name = %s, patient_surname = %s, phone_number = %s, appointment_date = %s, doctor_id = %s, service_id = %s
                           WHERE id = %s'''
                cursor.execute(query, (patient_name, patient_surname, phone_number, appointment_date, doctor_id, service_id, record_id))
                if cursor.rowcount == 0:
                    return False, "Запись с указанным id не найдена"
                conn.commit()
                return True, None

        except Exception as e:
            print(f"Ошибка при обновлении записи: {str(e)}")
            return False, str(e)

        finally:
            conn.close()

    @staticmethod
    def delete_record(record_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = '''DELETE FROM records WHERE id = %s'''
                cursor.execute(query, (record_id,))
                if cursor.rowcount == 0:
                    return False, "Запись с указанным id не найдена"
                conn.commit()
                return True, None

        except Exception as e:
            print(f"Ошибка при удалении записи: {str(e)}")
            return False, str(e)

        finally:
            conn.close()
