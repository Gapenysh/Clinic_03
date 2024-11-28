from psycopg2 import Error

from Clinic.db_connection import connection_db

def formate_data(result, colnames):
    formated_data = [
        dict(zip(colnames, row))
        for row in result
    ]
    return formated_data
class DoctorDAL(object):
    @staticmethod
    def get_doctors():
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = "SELECT * FROM doctor"

                cursor.execute(query)
                colnames = [desc[0] for desc in cursor.description]

                doctors_data = cursor.fetchall()

                doctors_data = formate_data(doctors_data, colnames)

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
                colnames = [desc[0] for desc in cursor.description]
                doctor_data = formate_data(doctor_data, colnames)

                return doctor_data, None

        except Exception as e:
            return None, str(e)

        finally:
            conn.close()


    @staticmethod
    def add_doctor(name: str, rating: int, edu: str, exp: int, speciality_id: int):
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt_doc = """INSERT INTO doctor(name, rating, education, experience)
                VALUES(%s, %s, %s, %s)
                RETURNING id;"""

                cur.execute(stmt_doc, (name, rating, edu, exp))
                doctor_id = cur.fetchone()
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
