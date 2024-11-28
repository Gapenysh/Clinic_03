from Clinic.db_connection import connection_db
def formate_data(result, colnames):
    formated_data = [
        dict(zip(colnames, row))
        for row in result
    ]
    return formated_data
class AnalyseDAL(object):
    @staticmethod
    def add_analyse(name: str, price: int, check_up_id: int):
        pass