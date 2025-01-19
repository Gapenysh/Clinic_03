from clinic.db_connection import connection_db
import psycopg2.extras

class AnalyseDAL(object):
    @staticmethod
    def get_analysis():
        conn = connection_db()

        try:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:  # Используем DictCursor
                query = '''
                    SELECT 
                        categories.id AS category_id,
                        categories.name AS category_name,
                        categories.description AS category_description,
                        analysis.id AS analysis_id,
                        analysis.name AS analysis_name,
                        analysis.price
                    FROM 
                        categories
                    JOIN 
                        analysis_categories ON categories.id = analysis_categories.category_id
                    JOIN 
                        analysis ON analysis.id = analysis_categories.analysis_id
                '''
                cursor.execute(query)
                analysis_data = cursor.fetchall()
                return analysis_data, None

        except Exception as e:
            return None, str(e)

        finally:
            conn.close()
