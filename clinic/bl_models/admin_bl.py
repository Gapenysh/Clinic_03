from clinic.dal_models.admin_dal import AdminDAL
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import check_password_hash, generate_password_hash


class AdminBL:
    @staticmethod
    def register_new_admin(email, name, password):
        password_hash = generate_password_hash(password)
        new_admin_id = AdminDAL.add_new_admin(email, name, password_hash)
        if new_admin_id:
            print(f"Новый админ создан: id = {new_admin_id}")
            return True
        else:
            return None

    @staticmethod
    def login(email, password):
        admin_id = AdminDAL.get_admin_by_email(email)
        if admin_id:
            hash_password = AdminDAL.get_password_by_admin_id(admin_id)
            if hash_password and AdminBL.check_password(hash_password, password):
                return AdminBL.create_tokens(admin_id)
        return None

    @staticmethod
    def create_tokens(user_id):
        access_token = create_access_token(identity=user_id)
        refresh_token = create_refresh_token(identity=user_id)
        return access_token, refresh_token

    @staticmethod
    def check_password(hash_password, password):
        return check_password_hash(hash_password, password)