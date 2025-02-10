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

    @staticmethod
    def get_actions():
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT 
                        a.id AS action_id,
                        a.photo,
                        a.description,
                        ac.name AS category_name
                    FROM 
                        actions a
                    JOIN 
                        actions_category ac ON a.category_id = ac.id;
                """
                cursor.execute(query)

                actions = [{"action_id": action_id, "photo": photo, "description": description, "category_name":
                   category_name} for action_id, photo, description, category_name in cursor.fetchall()]

                return actions, None

        except Exception as e:
            conn.rollback()
            return None, str(e)

        finally:
            conn.close()

    @staticmethod
    def delete_action(action_id: int):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = """
                    DELETE FROM actions WHERE id = %s
                """
                cursor.execute(query, (action_id,))
                conn.commit()

                return True, None

        except Exception as e:
            conn.rollback()
            return None, str(e)

        finally:
            conn.close()