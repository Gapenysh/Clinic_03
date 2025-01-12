from Clinic.dal_models.analysis_dal import AnalyseDAL


class AnalyseBL(object):
    @staticmethod
    def get_analysis():
        analysis_data, error = AnalyseDAL.get_analysis()
        if error:
            return None, error

        # Преобразование кортежей в словари
        keys = ["category_id", "category_name", "analysis_id", "analysis_name", "price"]
        analysis_data = [dict(zip(keys, row)) for row in analysis_data]

        # Структурируем данные в JSON формат
        result = {}
        for row in analysis_data:
            category_id = row["category_id"]
            if category_id not in result:
                result[category_id] = {
                    "id": category_id,
                    "name": row["category_name"],
                    "analyses": []
                }

            result[category_id]["analyses"].append({
                "id": row["analysis_id"],
                "name": row["analysis_name"],
                "price": row["price"]
            })

        return list(result.values()), None
