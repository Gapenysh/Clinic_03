from Clinic.dal_models.services_dal import ServiceDal

class ServiceBL:

    @staticmethod
    def get_specialities():
        data, error = ServiceDal.get_all_specialities()
        if error:
            return None, error

        # Преобразование данных в удобный JSON-формат
        result = {}
        for row in data:
            specialty_id = row["specialty_id"]
            if specialty_id not in result:
                result[specialty_id] = {
                    "id": specialty_id,
                    "name": row["specialty_name"],
                    "services": []
                }

            if row["service_id"]:
                result[specialty_id]["services"].append({
                    "id": row["service_id"],
                    "name": row["service_name"],
                    "price": row["price"]
                })

        return list(result.values()), None
