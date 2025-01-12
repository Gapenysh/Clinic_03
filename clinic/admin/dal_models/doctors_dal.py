from psycopg2 import Error

from clinic.db_connection import connection_db


class DoctorDAL(object):
    @staticmethod
    def add_doctor(
            full_name: str,
            specialties_id: list,
            experience: int,
            qualifications: list,
            phone_number: str,
            image: str
    ):
        if not isinstance(specialties_id, list) or not specialties_id:
            return None, "specialties_id should be a non-empty list"

        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = '''INSERT INTO doctors (phone_number, image, full_name, experience) 
                           VALUES (%s, %s, %s, %s) RETURNING id'''
                cursor.execute(query, (phone_number, image, full_name, experience))
                doctor_id = cursor.fetchone()[0]

                query = '''INSERT INTO doctor_specialties (doctor_id, speciality_id) VALUES (%s, %s)'''
                cursor.executemany(query, [(doctor_id, speciality_id) for speciality_id in specialties_id])

                query = '''INSERT INTO qualifications (doctor_id, name, year) VALUES (%s, %s, %s)'''
                cursor.executemany(query, [(doctor_id, qualification, year) for qualification, year in qualifications])

                conn.commit()

                return doctor_id, None

        except Exception as e:
            print(f"Error adding doctor: {str(e)}")
            return None, str(e)

        finally:
            conn.close()


    @staticmethod
    def update_doctor(
            doctor_id: int,
            full_name: str,
            specialties_id: list,
            experience: int,
            qualifications: list,
            phone_number: str,
            image: str
    ):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                # Обновление данных в таблице doctors
                query = '''UPDATE doctors
                           SET phone_number = %s, image = %s, full_name = %s, experience = %s
                           WHERE id = %s'''
                cursor.execute(query, (phone_number, image, full_name, experience, doctor_id))

                # Добавление новых специальностей
                if specialties_id:
                    query = '''INSERT INTO doctor_specialties (doctor_id, speciality_id) VALUES (%s, %s)'''
                    cursor.executemany(query, [(doctor_id, speciality_id) for speciality_id in specialties_id])


                # Добавление новых квалификаций
                if qualifications:
                    query = '''INSERT INTO qualifications (doctor_id, name, year) VALUES (%s, %s, %s)'''
                    cursor.executemany(query,
                                       [(doctor_id, qualification, year) for qualification, year in qualifications])

                conn.commit()

                return True, None

        except Exception as e:
            print(f"Error updating doctor: {str(e)}")
            return False, str(e)

        finally:
            conn.close()

    @staticmethod
    def delete_doctor(doctor_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = '''DELETE FROM doctors WHERE id = %s'''
                cursor.execute(query, (doctor_id,))

                conn.commit()

                return True, None

        except Exception as e:
            print(f"Error deleting doctor: {str(e)}")
            return False, str(e)

        finally:
            conn.close()