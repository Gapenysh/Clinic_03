from psycopg2 import Error
from clinic.db_connection import connection_db

class ServiceDAL(object):
    @staticmethod
    def get_services():
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = '''
                        SELECT
                            s.id,
                            s.service_name,
                            s.price,
                            sp.speciality_name
                        FROM
                            services s
                        JOIN
                            specialties sp ON s.speciality_id = sp.id
                    '''
                cursor.execute(query)
                results = cursor.fetchall()
                services_list = []

                for id, service_name, price, speciality_name in results:
                    services_list.append({
                        "id": id,
                        "name": service_name,
                        "price": price,
                        "speciality": speciality_name
                    })
                return services_list, None

        except Exception as e:
            print(f"Ошибка при получении услуг с специальностями: {str(e)}")
            return None, str(e)

        finally:
            conn.close()

    @staticmethod
    def add_service(service_name: str, price: int, speciality_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = '''INSERT INTO services (service_name, price, speciality_id)
                           VALUES (%s, %s, %s) RETURNING id'''
                cursor.execute(query, (service_name, price, speciality_id))
                result = cursor.fetchone()
                if result is not None:
                    service_id = result[0]
                    conn.commit()
                    return service_id, None
                else:
                    return None, "Не удалось добавить услугу: результат запроса пуст"

        except Exception as e:
            print(f"Ошибка при добавлении услуги: {str(e)}")
            return None, str(e)

        finally:
            conn.close()

    @staticmethod
    def update_service(service_id: int, service_name: str, price: int, speciality_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = '''UPDATE services
                           SET service_name = %s, price = %s, speciality_id = %s
                           WHERE id = %s'''
                cursor.execute(query, (service_name, price, speciality_id, service_id))
                if cursor.rowcount == 0:
                    return False, "Услуга с указанным id не найдена"
                conn.commit()
                return True, None

        except Exception as e:
            print(f"Ошибка при обновлении услуги: {str(e)}")
            return False, str(e)

        finally:
            conn.close()

    @staticmethod
    def delete_service(service_id: int):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = '''DELETE FROM services WHERE id = %s'''
                cursor.execute(query, (service_id,))
                if cursor.rowcount == 0:
                    return False, "Услуга с указанным id не найдена"
                conn.commit()
                return True, None

        except Exception as e:
            print(f"Ошибка при удалении услуги: {str(e)}")
            return False, str(e)

        finally:
            conn.close()
