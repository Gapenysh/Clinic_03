from Clinic.dal_models.analysis_dal import AnalyseDAL

class AnalyseBL(object):
    @staticmethod
    def add_analyse(name: str, price: int, check_up_id: int):

        analyse_id, error = AnalyseDAL.add_analyse(name, price, check_up_id)

        if error is None:
            return analyse_id, None

        return