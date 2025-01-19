from clinic.db_connection import connection_db


class ActionDAL(object):
    @staticmethod
    def add_actions(photo: str, description: str, category_id: int):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "INSERT INTO actions (photo, description, category_id) VALUES (%s, %s, %s) RETURNING id"
                cursor.execute(query, (photo, description, category_id))

                result = cursor.fetchone()
                if result is not None:
                    action_id = result[0]
                    conn.commit()
                    return action_id, None
                else:
                    conn.rollback()
                    return None, "Не удалось добавить действие: результат запроса пуст"

        except Exception as e:
            conn.rollback()
            print(f"Ошибка при добавлении действия: {str(e)}")
            return None, str(e)
        finally:
            conn.close()



