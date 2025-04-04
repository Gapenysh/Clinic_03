from clinic.dal_models.services_dal import ServiceDAL

class ServiceBL:
    @staticmethod
    def get_specialities(specialty_id=None):
        data, error = ServiceDAL.get_all_specialities(specialty_id)
        if error:
            return None, error

        result = {}
        for row in data:
            speciality_id = row["speciality_id"]
            if speciality_id not in result:
                result[speciality_id] = {
                    "id": speciality_id,
                    "name": row["speciality_name"],
                    "services": []
                }

            if row["service_id"]:
                result[speciality_id]["services"].append({
                    "id": row["service_id"],
                    "name": row["service_name"],
                    "price": row["price"]
                })

        return list(result.values()), None

    @staticmethod
    def get_specialties():
        specialties_data, error = ServiceDAL.get_specialties()

        if error is None:
            return specialties_data, None
        else:
            return False, error
