import logging

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

                    if doctor["filials"] is not None:
                        filial_list = doctor["filials"].split(',')
                    else:
                        filial_list = []
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

    @staticmethod
    def get_doctors():
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT id, id_easyclinic, full_name, photo, experiance, phone_number
                    FROM doctors;
                """
                cursor.execute(query)
                doctors_data = [
                    {
                        "id": id,
                        "id_easyclinic": id_easyclinic,
                        "name": full_name,
                        "photo": photo,
                        "experiance": experiance,
                        "phone": phone
                    }
                    for id, id_easyclinic, full_name, photo, experiance, phone in cursor.fetchall()
                ]

                # Получаем специализации для каждого врача
                query = """
                    SELECT s.name
                    FROM specialties s
                    JOIN doctor_speciality ds ON s.id = ds.speciality_id
                    WHERE ds.doctor_id = %s;
                """
                for doctor in doctors_data:
                    cursor.execute(query, (doctor["id"],))
                    specialties = cursor.fetchall()
                    doctor["specialties"] = [spec[0] for spec in specialties]

                # Получаем образование для каждого врача
                query = """
                    SELECT name, year 
                    FROM educations 
                    WHERE doctor_id = %s;
                """
                for doctor in doctors_data:
                    cursor.execute(query, (doctor["id"],))
                    educations = cursor.fetchall()
                    doctor["educations"] = [{"name": name, "year": year} for name, year in educations]

                return doctors_data

        except Exception as e:
            logging.error(f"Error fetching doctors data: {e}")
            return str(e)

        finally:
            conn.close()

    @staticmethod
    def edit_doctor(doctor_id: int, data: dict):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = """
                    UPDATE doctors 
                    SET full_name = %s, photo = %s, experiance = %s, phone_number = %s
                    WHERE id = %s;
                """
                cursor.execute(query, (
                    data["full_name"],
                    data["photo"],
                    data["experiance"],
                    data["phone_number"],
                    doctor_id
                ))


                if 'education' in data:
                    cursor.execute("DELETE FROM educations WHERE doctor_id = %s", (doctor_id,))
                    query = """
                        INSERT INTO educations (name, year, doctor_id) 
                        VALUES (%s, %s, %s)
                    """
                    for education in data["education"]:
                        cursor.execute(query, (
                            education["name"],
                            education["year"],
                            doctor_id
                        ))

                conn.commit()
                return 1

        except Exception as e:
            return str(e)
        finally:
            conn.close()