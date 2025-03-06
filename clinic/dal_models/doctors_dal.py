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
    def get_doctors_by_specialty(specialty_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = """
                        SELECT d.* 
                        FROM doctors d
                        JOIN doctor_speciality ds ON d.id = ds.doctor_id
                        WHERE ds.speciality_id = %s
                    """
                cursor.execute(query, (specialty_id,))
                doctors_data = cursor.fetchall()

                columns = [desc[0] for desc in cursor.description]
                doctors_list = [dict(zip(columns, row)) for row in doctors_data]

                return doctors_list

        except Exception as e:
            return str(e)

        finally:
            conn.close()

    @staticmethod
    def get_reviews():
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT r.id, r.patient_name_and_phone, r.time, r.content, r.doctor_id
                    FROM reviews r
                    """
                cursor.execute(query)
                reviews_data = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                reviews_list = [dict(zip(columns, row)) for row in reviews_data]
                return reviews_list

        except Exception as e:
            return str(e)

        finally:
            conn.close()

    @staticmethod
    def get_reviews_by_doctor(doctor_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT r.id, r.patient_name_and_phone, r.time, r.content, r.doctor_id
                    FROM reviews r
                    WHERE r.doctor_id = %s
                    """
                cursor.execute(query, (doctor_id,))
                reviews_data = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                reviews_list = [dict(zip(columns, row)) for row in reviews_data]
                return reviews_list

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
                    SELECT ds.doctor_id, s.name as specialty_name, s.id
                    FROM doctor_speciality ds
                    JOIN specialties s ON ds.speciality_id = s.id
                    """
                cursor.execute(query)
                specialties_data = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                specialties_list = [dict(zip(columns, row)) for row in specialties_data]
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
                    SELECT s.name, s.id
                    FROM specialties s
                    JOIN doctor_speciality ds ON s.id = ds.speciality_id
                    WHERE ds.doctor_id = %s
                """
                cursor.execute(query, (doctor_id,))
                specialties = cursor.fetchall()
                doctor_dict["specialties"] = [{"name": spec[0], "id": spec[1]} for spec in specialties]

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

    @staticmethod
    def get_doctors_for_main():
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT d.id, d.id_easyclinic, d.full_name, d.photo, s.name as specialty_name
                    FROM doctors d
                    LEFT JOIN doctor_speciality ds ON d.id = ds.doctor_id
                    LEFT JOIN specialties s ON ds.speciality_id = s.id
                """
                cursor.execute(query)
                doctors_data = cursor.fetchall()

                doctors_dict = {}
                for row in doctors_data:
                    doctor_id = row[0]
                    if doctor_id not in doctors_dict:
                        doctors_dict[doctor_id] = {
                            "id": row[0],
                            "id_easyclinic": row[1],
                            "full_name": row[2],
                            "photo": row[3],
                            "specialties": []
                        }
                    if row[4]:  # Если есть специальность, добавляем её
                        doctors_dict[doctor_id]["specialties"].append(row[4])

                # Обернем данные в объект с ключом "doctors"
                result = {"doctors": list(doctors_dict.values())}
                return result

        except Exception as e:
            return {"error": str(e)}

        finally:
            conn.close()

    @staticmethod
    def get_doctors_for_record(specialty_id=None):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                if specialty_id:
                    query = """
                                SELECT d.id, d.id_easyclinic, d.full_name 
                                FROM doctors d
                                JOIN doctor_speciality ds ON d.id = ds.doctor_id
                                WHERE ds.speciality_id = %s
                            """
                    cursor.execute(query, (specialty_id,))

                else:
                    query = "SELECT id, id_easyclinic, full_name FROM doctors"
                    cursor.execute(query)

                doctors = cursor.fetchall()

                return [{"id": doc[0], "id_easyclinic": doc[1], "full_name": doc[2]} for doc in doctors]

        except Exception as e:
            return {"error": str(e)}

        finally:
            conn.close()