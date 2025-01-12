from clinic.dal_models.services_dal import ServiceDAL

class ServiceBL:

    @staticmethod
    def get_specialities():
        data, error = ServiceDAL.get_all_specialities()
        if error:
            return None, error

        # Преобразование данных в удобный JSON-формат
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
