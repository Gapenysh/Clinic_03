from clinic.db_connection import connection_db


class AnalyseDAL(object):
    @staticmethod
    def get_all_analysis():
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = '''
                    SELECT
                        a.id AS analysis_id,
                        a.name AS analysis_name,
                        a.price AS analysis_price,
                        c.name AS category_name
                    FROM
                        analysis a
                    JOIN
                        analysis_categories ac ON a.id = ac.analysis_id
                    JOIN
                        categories c ON ac.category_id = c.id;
                '''
                cursor.execute(query)
                analysis_data = [{"id": analysis_id, "name": analysis_name, "price": analysis_price,
                                  "category": category_name} for analysis_id, analysis_name,
                                  analysis_price, category_name in cursor.fetchall()]

            return analysis_data, None

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
            conn.rollback()
            return None, str(e)

        finally:
            conn.close()

    @staticmethod
    def create_analysis(name: str, price: int, categories_id: list):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "INSERT INTO analysis (name, price) VALUES (%s, %s) RETURNING id;"
                cursor.execute(query, (name, price))
                analyse_id = cursor.fetchone()[0]

                for category_id in categories_id:
                    query = "INSERT INTO analysis_categories (analysis_id, category_id) VALUES (%s, %s)"
                    cursor.execute(query, (analyse_id, category_id))

                conn.commit()
                return analyse_id, None

        except Exception as e:
            conn.rollback()
            return None, str(e)
        finally:
            conn.close()

    @staticmethod
    def update_analysis(analysis_id: int, name: str, price: int, categories_id: list):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "UPDATE analysis SET name = %s, price = %s WHERE id = %s;"
                cursor.execute(query, (name, price, analysis_id))

                query = "DELETE FROM analysis_categories WHERE analysis_id = %s;"
                cursor.execute(query, (analysis_id,))

                for category_id in categories_id:
                    query = "INSERT INTO analysis_categories (analysis_id, category_id) VALUES (%s, %s);"
                    cursor.execute(query, (analysis_id, category_id))

                conn.commit()
                return True, None

        except Exception as e:
            conn.rollback()
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


    @staticmethod
    def delete_analyse(analyse_id):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "DELETE FROM analysis WHERE id = %s;"
                cursor.execute(query, (analyse_id,))
                conn.commit()
                return True, None

        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            conn.close()


    @staticmethod
    def delete_category(category_id):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = "DELETE FROM categories WHERE id = %s;"
                cursor.execute(query, (category_id,))
                conn.commit()
                return True, None
        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            conn.close()
