from psycopg2 import Error

from clinic.db_connection import connection_db


class DoctorDAL(object):
    @staticmethod
    def add_specialties(specialties):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "SELECT name FROM specialties"
                cursor.execute(query)
                specialties_name = [row[0] for row in cursor.fetchall()]

                query = "INSERT INTO specialties (name) VALUES (%s)"
                for speciality in specialties["specialities"]:
                    if speciality in specialties_name:
                        continue
                    cursor.execute(query, (speciality,))

                conn.commit()
                return 1

        except Exception as e:
            return str(e)
        finally:
            conn.close()


    @staticmethod
    def add_branches(branches):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "SELECT id_easyclinic FROM filials"
                cursor.execute(query)
                branches_id = [row[0] for row in cursor.fetchall()]

                query = "INSERT INTO filials (id_easyclinic, name) VALUES (%s, %s)"
                for branch in branches["filials"]:
                    if int(branch["id"]) in branches_id:
                        continue
                    cursor.execute(query, (branch["id"], branch["title"]))

                conn.commit()

                return 1

        except Exception as e:
            return str(e)
        finally:
            conn.close()


    @staticmethod
    def add_doctors(doctors):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "SELECT full_name FROM doctors;"
                cursor.execute(query)
                doctors_names = [row[0] for row in cursor.fetchall()]

                query = "SELECT id, id_easyclinic FROM filials"
                cursor.execute(query)
                filials_ids_bd = [list(row) for row in cursor.fetchall()]

                query = "SELECT * FROM specialties"
                cursor.execute(query)
                specialties_bd = [list(row) for row in cursor.fetchall()]

                query_doctors = "INSERT INTO doctors (id_easyclinic, full_name) VALUES (%s, %s) RETURNING id"
                for doctor in doctors["doctors"]:
                    if doctor['fio'] in doctors_names:
                        continue

                    cursor.execute(query_doctors, (doctor['id'], doctor['fio']))
                    doctor_id = cursor.fetchone()

                    filial_list = doctor["filials"].split(',')
                    for filial in filial_list:
                        query_filial = "INSERT INTO doctor_filial (doctor_id, filial_id) VALUES (%s, %s)"

                        for id, id_easyclinic in filials_ids_bd:
                            if int(id_easyclinic) == int(filial):
                                filial_id_bd = id
                                break


                        cursor.execute(query_filial, (doctor_id, filial_id_bd))

                    speciality = doctor['speciality']
                    query_speciality = "INSERT INTO doctor_speciality (doctor_id, speciality_id) VALUES (%s, %s)"
                    for id, name in specialties_bd:
                        if speciality == name:
                            speciality_id_bd = id

                    cursor.execute(query_speciality, (doctor_id, speciality_id_bd))

            conn.commit()

            return 1

        except Exception as e:
            return str(e)

        finally:
            conn.close()