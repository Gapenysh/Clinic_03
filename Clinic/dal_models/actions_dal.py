from clinic.db_connection import connection_db
from psycopg2 import Error


class ActionDAL:
    @staticmethod
    def get_actions():
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = '''
                    SELECT 
                        ac.id AS category_id,
                        ac.name AS category_name,
                        a.id AS action_id,
                        a.photo AS action_photo,
                        a.description AS action_description
                    FROM 
                        actions_category ac
                    LEFT JOIN 
                        actions a ON ac.id = a.category_id
                    ORDER BY 
                        ac.id, a.id;
                '''
                cursor.execute(query)
                data = cursor.fetchall()

                # Формируем JSON-структуру
                result = {}
                for row in data:
                    category_id = row[0]
                    if category_id not in result:
                        result[category_id] = {
                            "id": category_id,
                            "name": row[1],
                            "actions": []
                        }

                    if row[2] is not None:
                        result[category_id]["actions"].append({
                            "id": row[2],
                            "photo": row[3],
                            "description": row[4]
                        })

                return list(result.values()), None

        except Exception as e:
            return None, str(e)
        finally:
            conn.close()

