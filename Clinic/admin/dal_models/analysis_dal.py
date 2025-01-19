from psycopg2 import Error
from unicodedata import category

from clinic.db_connection import connection_db


class AnalyseDAL(object):
    @staticmethod
    def get_all_analyses():
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "SELECT id, name, price FROM analysis;"
                cursor.execute(query)
                analyses = cursor.fetchall()
                return analyses, None
        except Exception as e:
            return None, str(e)
        finally:
            conn.close()

    @staticmethod
    def get_all_categories():
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "SELECT id, name, description FROM categories;"
                cursor.execute(query)
                categories = cursor.fetchall()
                return categories, None
        except Exception as e:
            return None, str(e)
        finally:
            conn.close()

    @staticmethod
    def create_category(name: str, description: str, analysis_id: list):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "INSERT INTO categories (name, description) VALUES (%s, %s) RETURNING id;"
                cursor.execute(query, (name, description))
                category_id = cursor.fetchone()[0]

                for analyse_id in analysis_id:
                    query = "INSERT INTO analysis_categories (analysis_id, category_id) VALUES (%s, %s)"
                    cursor.execute(query, (analyse_id, category_id))


                conn.commit()
                return category_id, None
        except Exception as e:
            return None, str(e)
        finally:
            conn.close()

    @staticmethod
    def update_category(category_id, name, description):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "UPDATE categories SET name = %s, description = %s WHERE id = %s;"
                cursor.execute(query, (name, description, category_id))
                conn.commit()
                return True, None
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def create_analysis(name, price):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "INSERT INTO analysis (name, price) VALUES (%s, %s) RETURNING id;"
                cursor.execute(query, (name, price))
                conn.commit()
                analysis_id = cursor.fetchone()[0]
                return analysis_id, None
        except Exception as e:
            return None, str(e)
        finally:
            conn.close()

    @staticmethod
    def update_analysis(analysis_id, name, price):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "UPDATE analysis SET name = %s, price = %s WHERE id = %s;"
                cursor.execute(query, (name, price, analysis_id))
                conn.commit()
                return True, None
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    @staticmethod
    def get_analysis_and_categories():
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = '''
                    SELECT 
                        analysis.name AS analysis_name,
                        categories.name AS category_name
                    FROM 
                        analysis
                    JOIN 
                        analysis_categories ON analysis.id = analysis_categories.analysis_id
                    JOIN 
                        categories ON categories.id = analysis_categories.category_id;
                '''
                cursor.execute(query)
                data = cursor.fetchall()
                return data, None
        except Exception as e:
            return None, str(e)
        finally:
            conn.close()
