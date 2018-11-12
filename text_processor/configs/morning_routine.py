from configs.default_config import Config
from get_text import get_random_text

class MorningConfig(Config):
    """ This config outputs the first two actions the agent takes each day """
    
    header = "Mornings"

    def GET_PARA_LIST(self, day: list) -> list:
        """Only the first two things the agent does each day"""
        sentence_list = []

        for action in day[:2]:
            sentence_list.append(get_random_text(action["action_name"]))

        return sentence_list