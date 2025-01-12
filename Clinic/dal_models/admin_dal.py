from Clinic.db_connection import connection_db
from werkzeug.security import check_password_hash
from psycopg2 import Error
from psycopg2.extras import RealDictCursor


class AdminDAL:
    @staticmethod
    def add_new_admin(email, name, password_hash):
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """INSERT INTO admins (email, name, password_hash) VALUES (%s, %s, %s) RETURNING id"""
                cur.execute(stmt, (email, name, password_hash))
                new_admin_id = cur.fetchone()[0]
                conn.commit()
                return new_admin_id
        except Error as e:
            conn.rollback()
            print(f"Ошибка при добавлении нового админа: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def get_admin_by_email(email):
        conn = connection_db()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                stmt = """SELECT COUNT(*) FROM admins WHERE email = %s"""
                cur.execute(stmt, (email,))
                count = cur.fetchone()[0]
                if count != 0:
                    return True
                else:
                    return None
        except Error as e:
            print(f"Ошибка при получении админа по email: {e}")
            return None
        finally:
            conn.close()
    @staticmethod
    def check_password(admin, password):
        # Здесь должен быть код для проверки пароля админа
        return check_password_hash(admin.password_hash, password)