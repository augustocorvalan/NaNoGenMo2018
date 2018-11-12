from get_text import get_random_text
from models.sample_model import model

class Config:
    """ Default config """

    header = "Everything That Happened:"
    model = model
    HEADER_SEPARATOR = '\n\n'
    CHAPTER_SEPARATOR = '\n\n'
    SECTION_SEPARATOR = '\n*\n'

    def SET_MODEL(self, model):
        self.model = model

    def FILTER_DAYS(self) -> list:
        """Default returns all days"""
        return self.model["days"]

    def GET_CHARACTER(self) -> str:
        """ Default character is agent """
        return "agent"

    def GET_PARA_LIST(self, day: list) -> list:
        """Default maps actions to text 1:1"""
        sentence_list = []

        for action in day:
            sentence_list.append(get_random_text(action["action_name"]))

        return sentence_list

    def PARA_TO_STR(self, para_list: list) -> str:
        """ Default is to join with empty space """
        return ' '.join(para_list)

    def SECTION_TO_STR(self, section_list: list) -> str:
        out = self.header
        out += self.HEADER_SEPARATOR

        for para in section_list:
            out += self.PARA_TO_STR(para)
            out += self.CHAPTER_SEPARATOR

        out += self.SECTION_SEPARATOR
        return out

