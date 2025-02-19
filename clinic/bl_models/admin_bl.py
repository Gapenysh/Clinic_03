from clinic.dal_models.admin_dal import AdminDAL
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash


class AdminBL:
    @staticmethod
    def register_new_admin(email, name, password):
        password_hash = generate_password_hash(password)
        print(password_hash)
        new_admin_id = AdminDAL.add_new_admin(email, name, password_hash)
        if new_admin_id:
            print(f"Новый админ создан: id = {new_admin_id}")
            return True
        else:
            return None

    @staticmethod
    def login(email, password):
        admin_id = AdminDAL.get_admin_by_email(email)
        print(f'ADMIN ID - {admin_id}')
        if admin_id:
            hash_password = AdminDAL.get_password_by_admin_id(admin_id)
            if hash_password and AdminBL.check_password(hash_password, password):
                return AdminBL.create_token(admin_id)

    @staticmethod
    def create_token(user_id):
        token = create_access_token(identity=user_id)
        return token

    @staticmethod
    def check_password(hash_password, password):
        return check_password_hash(hash_password, password)