from Clinic.dal_models.service_dal import ServiceDal

class ServiceBL:

    @staticmethod
    def get_specialities():
        specialities, error = ServiceDal.get_all_specialities()
        if specialities:
            return specialities
        else:
            print(error)
            return None
    @staticmethod
    def get_services(speciality_id:int):
        services, error = ServiceDal.get_services(speciality_id)
        if services:
            return services
        else:
            print(error)
            return None