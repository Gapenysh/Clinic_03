from clinic.admin.dal_models.analysis_dal import AnalyseDAL


class AnalyseBL(object):
    @staticmethod
    def get_all_analyses():
        return AnalyseDAL.get_all_analyses()

    @staticmethod
    def get_all_categories():
        return AnalyseDAL.get_all_categories()

    @staticmethod
    def create_category(name: str, description: str, analysis: list):
        return AnalyseDAL.create_category(name, description, analysis)

    @staticmethod
    def update_category(category_id: int, name: str, description: str, analysis: list):
        return AnalyseDAL.update_category(category_id, name, description)

    @staticmethod
    def create_analysis(name, price):
        return AnalyseDAL.create_analysis(name, price)

    @staticmethod
    def update_analysis(analysis_id, name, price):
        return AnalyseDAL.update_analysis(analysis_id, name, price)

    @staticmethod
    def get_analysis_and_categories():
        return AnalyseDAL.get_analysis_and_categories()
