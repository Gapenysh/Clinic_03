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