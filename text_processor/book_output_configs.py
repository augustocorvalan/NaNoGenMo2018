from chapter_configs.default_config import Config
from chapter_configs.morning_routine import MorningConfig

from models._1_day_01 import model as model_1_01
from models._1_day_02 import model as model_1_02

from models._2_day_01 import model as model_2_01
from models._2_day_02 import model as model_2_02
from models._2_day_03 import model as model_2_03

from models._3_day_01 import model as model_3_01
from models._3_day_02 import model as model_3_02

import datetime

def output_file(input: str):
    # Open a file
    current_time = str(datetime.datetime.now())
    output_folder = 'text_processor/generated_files/'
    #output_folder =''
    file_name = output_folder + current_time + '.txt'

    fo = open(file_name, "w")
    fo.write(input)

    # Close opend file
    fo.close()


### SINKS ###
def terminal_sink(input: str):
    """ Default is to print to stdout"""
    print(input)

def latex_sink(input: str):
    """ outputs latex file """
    pass


### Formatters ###
def star_separator_formatter(lst: list) -> str:
    return '\n*\n'.join(lst)

def unordered_list_formatter(lst: list) -> str:
    return '\n\n'.join(lst)

def new_page_formatter(lst: list) -> str:
    return '\n###\n\n\n\n'.join(lst)


default_book_output_config = {
    "output_sink": terminal_sink,
    "chapter_list_to_string": new_page_formatter,
    "default_paragraph_formatter": unordered_list_formatter,
    "default_section_formatter": star_separator_formatter,
    "chapter_configs": [
        { "config": MorningConfig, "model": model_1_01 },
        { "config": MorningConfig, "model": model_1_02 },
        { "config": Config },
        { "config": MorningConfig, "model": model_2_01 },
        { "config": Config },
        { "config": MorningConfig, "model": model_2_02 },
        { "config": MorningConfig, "model": model_3_01 },
        { "config": Config, "model": model_3_01 },
        { "config": MorningConfig, "model": model_3_02 },
        { "config": Config, "model": model_3_02 },
    ]
}
