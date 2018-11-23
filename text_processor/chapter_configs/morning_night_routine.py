from chapter_configs.default_config import Config
from get_text import get_random_text

class MorningNightConfig(Config):
    """ This config outputs the first two actions the agent takes each day """
    
    header = "Mornings"

    def GET_PARA_LIST(self, day: list) -> list:
        """Only the first two things the agent does each day plus the last"""
        sentence_list = []

        for action in day[:2]:
            sentence_list.append(get_random_text(action["action_name"]))

        # also get the last action 
        sentence_list.append(get_random_text(day[-1]['action_name']))


        return sentence_list