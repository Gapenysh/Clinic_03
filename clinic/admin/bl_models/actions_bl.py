from clinic.admin.dal_models.actions_dal import ActionDAL


class ActionBL(object):
    @staticmethod
    def add_action(photo: str, description: str, category_id: int):
        return ActionDAL.add_actions(photo, description, category_id)


    @staticmethod
    def get_action():
        return ActionDAL.get_actions()


    @staticmethod
    def delete_action(action_id: int):
        return ActionDAL.delete_action(action_id)


    @staticmethod
    def get_categories():
        return ActionDAL.get_categories()