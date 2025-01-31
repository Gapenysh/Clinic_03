from certifi import contents
from psycopg2 import Error

from clinic.db_connection import connection_db


class DoctorDAL(object):
    @staticmethod
    def get_doctors():
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = "SELECT * FROM doctors"
                cursor.execute(query)
                doctors_data = cursor.fetchall()

                columns = [desc[0] for desc in cursor.description]
                doctors_list = [dict(zip(columns, row)) for row in doctors_data]

                return doctors_list

        except Exception as e:
            return str(e)

        finally:
            conn.close()

    @staticmethod
    def get_specialties():
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT ds.doctor_id, s.name as specialty_name
                    FROM doctor_speciality ds
                    JOIN specialties s ON ds.speciality_id = s.id
                    """
                cursor.execute(query)
                specialties_data = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                specialties_list = [dict(zip(columns, row)) for row in specialties_data]
                print(f"specialties_list dal - {specialties_list}")
                return specialties_list

        except Exception as e:
            return str(e)
        finally:
            conn.close()

    @staticmethod
    def get_filials():
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT df.doctor_id, f.name as filial_name
                    FROM doctor_filial df
                    JOIN filials f ON df.filial_id = f.id
                    """
                cursor.execute(query)
                filials_data = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                filials_list = [dict(zip(columns, row)) for row in filials_data]
                print(f"filial list dal - {filials_list}")
                return filials_list
        except Exception as e:
            return str(e)
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

                if not doctor_data:
                    return {"error": "Doctor not found"}

                columns = [desc[0] for desc in cursor.description]
                doctor_dict = dict(zip(columns, doctor_data))

                query = """
                    SELECT s.name 
                    FROM specialties s
                    JOIN doctor_speciality ds ON s.id = ds.speciality_id
                    WHERE ds.doctor_id = %s
                """
                cursor.execute(query, (doctor_id,))
                specialties = cursor.fetchall()
                doctor_dict["specialties"] = [spec[0] for spec in specialties]

                query = """
                    SELECT f.name 
                    FROM filials f
                    JOIN doctor_filial df ON f.id = df.filial_id
                    WHERE df.doctor_id = %s
                """
                cursor.execute(query, (doctor_id,))
                filials = cursor.fetchall()
                doctor_dict["filials"] = [filial[0] for filial in filials]

                query = """
                        SELECT name, year FROM educations WHERE doctor_id = %s;
                """
                cursor.execute(query, (doctor_id,))
                educations = [{"name": name, "year": year} for name, year in cursor.fetchall()]
                doctor_dict["education"] = educations

                query = """
                    SELECT patient_name_and_phone, time, content FROM reviews WHERE doctor_id = %s
                """
                cursor.execute(query, (doctor_id,))
                reviews = [{"patient_info": patient_info, "time": time, "content": content} for patient_info, time, content in cursor.fetchall()]
                doctor_dict["reviews"] = reviews

                return doctor_dict

        except Exception as e:
            return {"error": str(e)}

        finally:
            conn.close()