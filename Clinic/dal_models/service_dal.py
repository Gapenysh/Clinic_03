from psycopg2 import Error

from Clinic.db_connection import connection_db


class ServiceDal:

    @staticmethod
    def get_all_specialities():
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT * FROM speciality"""
                cur.execute(stmt)
                result = cur.fetchall()
                return result, None
        except Error as e:
            return None, str(e)
        finally:
            conn.close()
    @staticmethod
    def get_services(doc_spec_id:int):
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT name, price FROM service WHERE doctor_specialty_id = %s"""
                cur.execute(stmt, (doc_spec_id,))
                result = cur.fetchall()
                return result, None
        except Error as e:
            return None, str(e)
        finally:
            conn.close()