from clinic.admin.dal_models.analysis_dal import AnalyseDAL


class AnalyseBL(object):
    @staticmethod
    def get_all_analysis():
        return AnalyseDAL.get_all_analysis()


    @staticmethod
    def get_all_categories():
        return AnalyseDAL.get_all_categories()


    @staticmethod
    def create_category(name: str, description: str, analysis: list):
        return AnalyseDAL.create_category(name, description, analysis)


    @staticmethod
    def update_category(category_id: int, name: str, description: str, analysis: list):
        return AnalyseDAL.update_category(category_id, name, description, analysis)


    @staticmethod
    def create_analysis(name: str, price: int, categories_id: list):
        return AnalyseDAL.create_analysis(name, price, categories_id)


    @staticmethod
    def update_analysis(analysis_id, name, price, categories_id: list):
        return AnalyseDAL.update_analysis(analysis_id, name, price, categories_id)


    @staticmethod
    def get_analysis_and_categories():
        return AnalyseDAL.get_analysis_and_categories()


    @staticmethod
    def delete_analyse(analyse_id: int):
        return AnalyseDAL.delete_analyse(analyse_id)


    @staticmethod
    def delete_category(category_id: int):
        return AnalyseDAL.delete_category(category_id)
