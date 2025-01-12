from psycopg2 import Error

from Clinic.db_connection import connection_db


class DoctorDAL(object):
    @staticmethod
    def get_doctors():
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = "SELECT * FROM doctors"
                cursor.execute(query)
                doctors_data = cursor.fetchall()
                return doctors_data, None

        except Exception as e:
            return None, str(e)

        finally:
            conn.close()

    @staticmethod
    def get_doctor(doctor_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = "SELECT * FROM doctors WHERE id = %s"
                cursor.execute(query, (doctor_id,))
                doctor_data = cursor.fetchone()
                return doctor_data, None

        except Exception as e:
            return None, str(e)

        finally:
            conn.close()

    @staticmethod
    def get_available_slots(doctor_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = "SELECT slot_date, slot_time FROM available_slots WHERE doctor_id = %s"
                cursor.execute(query, (doctor_id,))
                slots_data = cursor.fetchall()
                # Преобразование данных в словари
                slots_data = [{'slot_date': row[0], 'slot_time': row[1]} for row in slots_data]
                return slots_data, None

        except Exception as e:
            return None, str(e)

        finally:
            conn.close()

    @staticmethod
    def get_qualification(doctor_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = "SELECT name, year FROM qualifications WHERE doctor_id = %s"
                cursor.execute(query, (doctor_id,))
                qualifications_data = cursor.fetchall()
                return qualifications_data, None

        except Exception as e:
            return None, str(e)

        finally:
            conn.close()


    @staticmethod
    def get_reviews(doctor_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = "SELECT patient_phone, date, review_content FROM reviews WHERE doctor_id = %s"
                cursor.execute(query, (doctor_id,))
                reviews_data = cursor.fetchall()
                return reviews_data, None

        except Exception as e:
            print(e)
            return None, str(e)


        finally:
            conn.close()

    @staticmethod
    def get_specialties(doctor_id: int):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                # Первый запрос: получаем speciality_id для данного doctor_id
                query = "SELECT speciality_id FROM doctor_specialties WHERE doctor_id = %s"
                cursor.execute(query, (doctor_id,))
                speciality_ids = cursor.fetchall()

                if not speciality_ids:
                    return [], None  # Нет специальностей для данного врача

                # Преобразуем результат в список speciality_id
                speciality_ids = [item[0] for item in speciality_ids]

                # Второй запрос: получаем информацию о специальностях
                placeholders = ','.join(['%s'] * len(speciality_ids))
                query = f"SELECT * FROM specialties WHERE id IN ({placeholders})"
                cursor.execute(query, speciality_ids)
                specialties_data = cursor.fetchall()

                return specialties_data, None

        except Exception as e:
            print(e)
            return None, str(e)
        finally:
            conn.close()


    @staticmethod
    def add_doctor(name: str, rating: int, edu: str, exp: int, speciality_id: int):
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt_doc = """INSERT INTO doctors(full_name, experience)
                VALUES(%s, %s)
                RETURNING id;"""
                cur.execute(stmt_doc, (name, exp))
                doctor_id = cur.fetchone()[0]

                stmt_doc_spec = """INSERT INTO speciality_doctor(doctor_id, speciality_id)
                VALUES(%s, %s)"""
                cur.execute(stmt_doc_spec, (doctor_id, speciality_id))
                conn.commit()
                return True
        except Error as e:
            print(str(e))
            return False
        finally:
            conn.close()

