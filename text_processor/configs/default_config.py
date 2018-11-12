from get_text import get_random_text

class Config:
    header = "Everything That Happened:"
    """ Default config """
    def __init__(self, model):
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
        out += '\n\n'
        for para in section_list:
            out += '\n'
            out += self.PARA_TO_STR(para)
            out += '\n'

        out += '*'
        return out

    def OUTPUT(self, input: str):
        """ Default is to print to stdout"""
        print(input)
