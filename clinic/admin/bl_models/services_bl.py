from clinic.admin.dal_models.services_dal import ServiceDAL

class ServiceBL(object):
    @staticmethod
    def get_services():
        return ServiceDAL.get_services()


    @staticmethod
    def add_service(service_name: str, price: int, speciality_id: int):
        service_id, error = ServiceDAL.add_service(service_name, price, speciality_id)

        if error is None:
            return service_id, None
        else:
            return None, error


    @staticmethod
    def update_service(service_id: int, service_name: str, price: int, speciality_id: int):
        success, error = ServiceDAL.update_service(service_id, service_name, price, speciality_id)

        if error is None:
            return True, None
        else:
            return False, error


    @staticmethod
    def delete_service(service_id: int):
        success, error = ServiceDAL.delete_service(service_id)

        if error is None:
            return True, None
        else:
            return False, error


    @staticmethod
    def get_specialties():
        specialties_data, error = ServiceDAL.get_specialties()

        if error is None:
            return specialties_data, None
        else:
            return False, error
