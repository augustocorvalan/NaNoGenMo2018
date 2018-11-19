from get_text import get_random_text
from chapter_configs.default_config import Config
from book_output_configs import default_book_output_config


BOOK_OUTPUT_CONFIG = default_book_output_config

def output_from_model(chapter_config) -> str:
    Config_class = chapter_config['config']
    config: Config = Config_class()
    model: dict = chapter_config.get('model')

    if (model):
        config.model = model

    days: list = config.FILTER_DAYS() # Example would be to only return first day

    section_list: list = []

    for day in days:
        para_list: list = []
        character_day: list = day[config.GET_CHARACTER()]
        para_list: list = config.GET_PARA_LIST(character_day)
        section_list.append(para_list)

    out = config.SECTION_TO_STR(section_list)

    return out


def output_book(book_output_config: dict, chapter_separator='\f', output_fn=None):
    output_fn = book_output_config['output_fn']
    chapters: list = book_output_config['chapter_configs']

    ## holds the stringified chapters we derive from the chapter configs
    chapter_string_list = []

    for chapter in chapters:
        chapter_string_list.append(output_from_model(chapter))

    book_str: str = chapter_separator.join(chapter_string_list)

    output_fn(book_str)



output_book(BOOK_OUTPUT_CONFIG)