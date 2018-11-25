from chapter_configs.default_config import Config
from chapter_configs.morning_routine import MorningConfig
from chapter_configs.morning_night_routine import MorningNightConfig 

from models._1_day_01 import model as model_1_01
from models._1_day_02 import model as model_1_02
from models._1_day_03 import model as model_1_03
from models._1_day_04 import model as model_1_04
from models._1_day_05 import model as model_1_05

from models._1_day_11 import model as model_1_11
from models._1_day_12 import model as model_1_12

from models._2_day_01 import model as model_2_01
from models._2_day_02 import model as model_2_02
from models._2_day_03 import model as model_2_03

from models._3_day_01 import model as model_3_01
from models._3_day_02 import model as model_3_02

import datetime

import os
import subprocess


def get_file_name(format='.txt') -> str:
    current_time = str(datetime.datetime.now())
    output_folder = './text_processor/generated_files/'
    file_name = os.path.abspath(output_folder) + '/' + current_time + format
    return file_name

def output_file(input: str, format='.txt'):
    current_time = str(datetime.datetime.now())
    output_folder = './text_processor/generated_files/'
    #output_folder =''
    file_name = output_folder + current_time + '.txt'

    fo = open(file_name, "w")
    fo.write(input)

    # Close opend file
    fo.close()


### SINKS ###
def log_sink(input: str):
    """ Default is to print to stdout"""
    print(input)

def latex_sink(input: str):
    """ outputs latex file """

    content = r'''
    \documentclass{article}
    \begin{document}
    %s
    \end{document}
    '''     

    file_name = get_file_name(format='.tex')
    print('FILE NAME!', file_name)
    with open(file_name,'w') as f:
        f.write(content%input)

    cmd = ['pdflatex', '-interaction', 'nonstopmode', file_name]
    proc = subprocess.Popen(cmd)
    proc.communicate()

    retcode = proc.returncode
    if not retcode == 0:
        raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

    os.unlink(file_name)


### Formatters ###
def star_separator_formatter(lst: list) -> str:
    return '\n*\n\n'.join(lst)

def unordered_list_formatter(lst: list) -> str:
    return '\n\n'.join(lst)

def new_page_formatter(lst: list) -> str:
    return '\n\n&&&&&&\n\n'.join(lst)

def latex_unordered_list_formatter(lst: list) -> str:
    content = r'''%s\\\\'''

    return ''.join(content%item for item in lst)


def latex_new_page_formatter(lst: list) -> str:
    content = r'''
    \section{}
    %s
    \newpage
    '''

    return ''.join(content%item for item in lst)


MORNING_ACTIONS = [
    'AGENT_WAKES',
    'AGENT_USES_BATHROOM',
    'AGENT_OBSERVES_SELF'
]
AFTERNOON_ACTIONS = [
    'AGENT_EATS',
    'AGENT_EXERCISES',
]
NIGHT_ACTIONS = [
    'AGENT_SLEEPS',
    'AGENT_DREAMS'
]
SURVEILLANCE_ACTIONS = [
    'AGENT_DISCOVERS_SURVEILLANCE',
]


latex_book_output_config = {
    "output_sink": latex_sink,
    "chapter_list_to_string": latex_new_page_formatter,
    "default_paragraph_formatter": latex_unordered_list_formatter,
    "default_section_formatter": star_separator_formatter,
    "chapter_configs": [
        # morning config, day 1
        { "include_actions": MORNING_ACTIONS, "model": model_1_11 },
        # morning night config, day 1
        { "include_actions": MORNING_ACTIONS + NIGHT_ACTIONS, "model": model_1_11 },
        # morning night surveillance config, day 1
        { "include_actions": MORNING_ACTIONS + SURVEILLANCE_ACTIONS + NIGHT_ACTIONS, "model": model_1_11 },

        # night
        { "include_actions": NIGHT_ACTIONS, "model": model_1_11 },

        # morning config, day 2
        { "include_actions": MORNING_ACTIONS, "model": model_1_12 },
        # morning afternoon night config, day 2
        { "include_actions": MORNING_ACTIONS + NIGHT_ACTIONS, "model": model_1_12 },
        # morning afternoon surveillance night config, day 2
        { "include_actions": MORNING_ACTIONS + SURVEILLANCE_ACTIONS + NIGHT_ACTIONS, "model": model_1_12 },

        # night
        { "include_actions": NIGHT_ACTIONS, "model": model_1_12 },

        # TODO machine description (break up paragraphs into individual sentences and format as ordered list)
        # TODO morning + night
        # TODO machine description
        # TODO machine description (funky formatter)

    ]
}

log_book_output_config = {
    "output_sink": log_sink,
    "chapter_list_to_string": new_page_formatter,
    "default_paragraph_formatter": unordered_list_formatter,
    "default_section_formatter": star_separator_formatter,
    "chapter_configs": [
        # morning config, day 1
        { "include_actions": MORNING_ACTIONS, "model": model_1_11 },
        # morning night config, day 1
        { "include_actions": MORNING_ACTIONS + NIGHT_ACTIONS, "model": model_1_11 },
        # morning night surveillance config, day 1
        { "include_actions": MORNING_ACTIONS + SURVEILLANCE_ACTIONS + NIGHT_ACTIONS, "model": model_1_11 },

        # night
        { "include_actions": NIGHT_ACTIONS, "model": model_1_11 },

        # morning config, day 2
        { "include_actions": MORNING_ACTIONS, "model": model_1_12 },
        # morning afternoon night config, day 2
        { "include_actions": MORNING_ACTIONS + NIGHT_ACTIONS, "model": model_1_12 },
        # morning afternoon surveillance night config, day 2
        { "include_actions": MORNING_ACTIONS + SURVEILLANCE_ACTIONS + NIGHT_ACTIONS, "model": model_1_12 },

        # night
        { "include_actions": NIGHT_ACTIONS, "model": model_1_12 },

        # dream, model 2, format no pagebreak
        # morning, night, dream, model 2




        # TODO machine description (break up paragraphs into individual sentences and format as ordered list)
        # TODO morning + night
        # TODO machine description
        # TODO machine description (funky formatter)
    ]
}




#default_book_output_config = log_book_output_config
default_book_output_config = latex_book_output_config 
