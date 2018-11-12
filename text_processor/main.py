from get_text import get_random_text
from configs.default_config import Config
from configs.morning_routine import MorningConfig


# GOAL: output only the first two things the agent does. para=2 sentences. 

def output_from_model(config_class):
    config: Config = config_class()

    days: list = config.FILTER_DAYS() # Example would be to only return first day

    section_list: list = []

    for day in days:
        para_list: list = []
        character_day: list = day[config.GET_CHARACTER()]
        para_list: list = config.GET_PARA_LIST(character_day)
        section_list.append(para_list)

    out = config.SECTION_TO_STR(section_list)

    config.OUTPUT(out)


output_from_model(MorningConfig)