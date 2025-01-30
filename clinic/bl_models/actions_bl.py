import logging

from clinic.dal_models.actions_dal import ActionDAL


class ActionBL(object):
    @staticmethod
    def get_actions():
        return ActionDAL.get_actions()

