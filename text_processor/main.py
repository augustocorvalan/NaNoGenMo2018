from models.sample_model import model as sample_model
from book_output_configs import default_book_output_config
from get_text import get_random_text

BOOK_OUTPUT_CONFIG = default_book_output_config

def chapter_from_config(book_config, chapter_config) -> str:
    paragraph_formatter = chapter_config['paragraph_formatter'] if 'paragraph_formatter' in chapter_config else book_config['default_paragraph_formatter']
    section_formatter = chapter_config['section_formatter'] if 'section_formatter' in chapter_config else book_config['default_section_formatter']
    include_actions = chapter_config['include_actions'] if 'include_actions' in chapter_config else []
    # get the model
    model = chapter_config['model'] if 'model' in chapter_config else sample_model
    # get days you want from the model
    days = chapter_config['days'] if 'days' in chapter_config else model["days"]
    # get the paragraphs for each section

    section_list: list = []
    for day in days:
        # filter out character
        character_day = day['agent'] # TODO hardcoded for now
        # get the action names
        action_names = [action['action_name'] for action in character_day]
        # get text for each action in character's day
        para_list = [get_random_text(action) for action in action_names if action in include_actions]
        # add paragraph to section
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