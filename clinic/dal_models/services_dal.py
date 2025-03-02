from clinic.db_connection import connection_db
import psycopg2.extras

class ServiceDAL:
    @staticmethod
    def get_all_specialities(specialty_id=None):
        conn = connection_db()
        try:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                query = '''
                        SELECT 
                            specialties.id AS speciality_id,
                            specialties.name AS speciality_name,
                            services.id AS service_id,
                            services.service_name,
                            services.price
                        FROM 
                            specialties
                        LEFT JOIN 
                            services ON specialties.id = services.speciality_id
                    '''

                params = []
                if specialty_id:
                    query += " WHERE specialties.id = %s"
                    params.append(specialty_id)

                cursor.execute(query, params)
                data = cursor.fetchall()

                return data, None
        except Exception as e:
            return None, str(e)
        finally:
            conn.close()

    @staticmethod
    def get_specialties():
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = '''SELECT * FROM specialties'''
                cursor.execute(query)

                specialties_data = [{"id": id, "name": name} for id, name in cursor.fetchall()]

                return specialties_data, None

        except Exception as e:
            print(f"Ошибка при удалении услуги: {str(e)}")
            return False, str(e)

        finally:
            conn.close()
