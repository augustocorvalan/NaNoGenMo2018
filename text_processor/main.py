from chapter_configs.default_config import Config
from book_output_configs import default_book_output_config

BOOK_OUTPUT_CONFIG = default_book_output_config

def chapter_from_config(book_config, chapter_config) -> str:
    paragraph_formatter = chapter_config['paragraph_formatter'] if 'paragraph_formatter' in chapter_config else book_config['default_paragraph_formatter']
    section_formatter = chapter_config['section_formatter'] if 'section_formatter' in chapter_config else book_config['default_section_formatter']
    # init config
    Config_class = chapter_config['config']
    config: Config = Config_class()
    # set the model on the config class if specified
    model: dict = chapter_config.get('model')
    if (model):
        config.model = model
    # get days you want
    days: list = config.FILTER_DAYS() # Example would be to only return first day
    # get the paragraphs for each section
    section_list: list = []
    for day in days:
        para_list: list = []
        # filter out character
        character_day: list = day[config.GET_CHARACTER()]
        para_list: list = config.GET_PARA_LIST(character_day)
        para_str: str = paragraph_formatter(para_list)
        section_list.append(para_str)
    # format section and return
    return section_formatter(section_list)

def get_chapters(book_config: dict) -> list:
    chapter_configs: list = book_config['chapter_configs']
    return [chapter_from_config(book_config, chapter_config) for chapter_config in chapter_configs]

def main(book_config):
    """ Anything that's logic lives here! """
    chapter_list_to_string = book_config['chapter_list_to_string']
    output_sink = book_config['output_sink']
    # get chapters
    chapters: list = get_chapters(book_config)
    # flatten out book
    output_string: str = chapter_list_to_string(chapters) # flattens chapter list w/ separator characters
    # output
    output_sink(output_string) # holds the logic to output to final format 

def run(mainFn, book_config):
    """ bootstrapping goes here! """
    mainFn(book_config)

run(main, book_config=default_book_output_config)