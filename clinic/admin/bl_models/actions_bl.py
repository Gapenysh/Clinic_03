from clinic.admin.dal_models.actions_dal import ActionDAL


class ActionBL(object):
    @staticmethod
    def add_action(photo: str, description: str, category_id: int):
        return ActionDAL.add_actions(photo, description, category_id)


