from Clinic.dal_models.admin_dal import AdminDAL
from flask_jwt_extended import create_access_token
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
        admin = AdminDAL.get_admin_by_email(email)
        if admin and AdminDAL.check_password(admin, password):
            return AdminBL.create_token(admin.id)
        else:
            return None

    @staticmethod
    def create_token(user_id):
        token = create_access_token(identity=user_id)
        return token