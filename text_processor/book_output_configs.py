from chapter_configs.default_config import Config
from chapter_configs.morning_routine import MorningConfig
from chapter_configs.morning_night_routine import MorningNightConfig 

from models._1_day_01 import model as model_1_01
from models._1_day_02 import model as model_1_02
from models._1_day_03 import model as model_1_03
from models._1_day_04 import model as model_1_04
from models._1_day_05 import model as model_1_05
from models._1_day_06 import model as model_1_06
from models._1_day_07 import model as model_1_07
from models._1_day_08 import model as model_1_08
from models._1_day_09 import model as model_1_09

from models._1_day_11 import model as model_1_11
from models._1_day_12 import model as model_1_12

from models._2_day_01 import model as model_2_01
from models._2_day_02 import model as model_2_02
from models._2_day_03 import model as model_2_03
from models._2_day_04 import model as model_2_04
from models._2_day_05 import model as model_2_05

from models._3_day_01 import model as model_3_01
from models._3_day_02 import model as model_3_02
from models._3_day_03 import model as model_3_03

from models._10_day_01 import model as model_10_01

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
    \usepackage{graphicx}

    \begin{document}
    \begin{titlepage}
    \centering
    \begin{center}
    {\huge\bfseries The Hallway \par}
    \end{center}
    \vspace{2cm}
    {\Large\itshape Augusto Corvalan\par}
    \vfill
    {\large November 2018\par}
    \end{titlepage}

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


def latex_single_paragraph_formatter(lst: list) -> str:
    content = r'''%s '''
    return ''.join(content%item for item in lst)

def latex_unordered_list_formatter(lst: list) -> str:
    content = r'''%s\\\\'''
    return ''.join(content%item for item in lst)

def latex_ordered_list_formatter(lst: list) -> str:
    content = r'''
    \item %s\\
    '''
    list_items = ''.join(content%item for item in lst)
    
    list_wrapper = r'''
    \begin{enumerate}
    %s
    \end{enumerate}
    '''

    return list_wrapper%list_items

def latex_single_space_list_formatter(lst: list) -> str:
    content = r'''%s\\'''
    return ''.join(content%item for item in lst)

def latex_new_page_formatter(lst: list) -> str:
    content = r'''
    \section{}
    %s
    \newpage
    '''

    return ''.join(content%item for item in lst)

def latex_no_page_break_formatter(lst: list) -> str:
    content = r'''
    %s
    '''

    return ''.join(content%item for item in lst)

def latex_get_repeated_list_formatter(numb: int):
    def latex_repeated_list_formatter(lst: list) -> str:
        return latex_unordered_list_formatter(lst * numb)
    return latex_repeated_list_formatter

def get_repeated_list_formatter(numb: int):
    def repeated_list_formatter(lst: list) -> str:
        return unordered_list_formatter(lst * numb)
    return repeated_list_formatter


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
MACHINE_ACTIONS = [
    'AGENT_DESCRIBES_MACHINE'
]
AGENCY_ACTIONS = [
    'AGENT_RECEIVES_DIRECTION',
    'AGENT_WRITES_REPORT',
    'AGENT_OBSERVES_REV',
    'AGENT_WRITES_REPORT'
]
OBSERVATION_ACTIONS = [
    'AGENT_OBSERVES_SELF',
    'AGENT_OBSERVES_SPACE',
    'AGENT_OBSERVES_REV'
]

chapter_configs = [
    # PART 1 - INTRO/MORNING ROUTINE
        { "include_actions": MORNING_ACTIONS, "model": model_1_11 },
        { "include_actions": MORNING_ACTIONS + NIGHT_ACTIONS, "model": model_1_11 },
        { "include_actions": MORNING_ACTIONS + SURVEILLANCE_ACTIONS + NIGHT_ACTIONS, "model": model_1_11 },

        { "include_actions": NIGHT_ACTIONS, "model": model_1_11 },

        { "include_actions": MORNING_ACTIONS + SURVEILLANCE_ACTIONS, "model": model_1_12 },
        { "include_actions": MORNING_ACTIONS + NIGHT_ACTIONS, "model": model_1_12 },
        { "include_actions": MORNING_ACTIONS + SURVEILLANCE_ACTIONS + NIGHT_ACTIONS, "model": model_1_12 },

        { "include_actions": NIGHT_ACTIONS, "model": model_1_12 },
    # END PART 1
    # PART 2 - AFTERNOON ROUTINE
        { 
            "include_actions": AGENCY_ACTIONS, 
            "model": model_1_05,
            "paragraph_formatter": latex_single_paragraph_formatter
        },
        { 
            "include_actions": MORNING_ACTIONS + AGENCY_ACTIONS, 
            "model": model_1_05,
            "paragraph_formatter": latex_single_paragraph_formatter
        },
        { 
            "include_actions": AFTERNOON_ACTIONS, 
            "model": model_10_01, 
            "paragraph_formatter": latex_single_paragraph_formatter, 
        },

        { "include_actions": SURVEILLANCE_ACTIONS + AFTERNOON_ACTIONS, "model": model_1_04, "paragraph_formatter": latex_single_paragraph_formatter },
        
        { "include_actions": AFTERNOON_ACTIONS, "model": model_1_04, "paragraph_formatter": latex_single_paragraph_formatter },

        { 
            "include_actions": AGENCY_ACTIONS, 
            "model": model_1_05,
            "paragraph_formatter": latex_single_paragraph_formatter
        },
        { 
            "include_actions": MORNING_ACTIONS + AGENCY_ACTIONS, 
            "model": model_1_05,
            "paragraph_formatter": latex_single_paragraph_formatter
        },

        { "include_actions": AFTERNOON_ACTIONS, "model": model_1_04, "paragraph_formatter": latex_single_paragraph_formatter },

        { "include_actions": NIGHT_ACTIONS, "model": model_1_11 },

        { 
            "include_actions": AFTERNOON_ACTIONS, 
            "model": model_10_01, 
            "paragraph_formatter": latex_single_paragraph_formatter, 
        },

        { "include_actions": SURVEILLANCE_ACTIONS + AFTERNOON_ACTIONS, "model": model_1_04, "paragraph_formatter": latex_single_paragraph_formatter },
        
        { "include_actions": AFTERNOON_ACTIONS, "model": model_1_04, "paragraph_formatter": latex_single_paragraph_formatter },

        { "include_actions": NIGHT_ACTIONS, "model": model_1_12 },
        
        { 
            "include_actions": OBSERVATION_ACTIONS + SURVEILLANCE_ACTIONS, 
            "model": model_10_01, 
            "paragraph_formatter": latex_single_paragraph_formatter, 
            "section_formatter": latex_unordered_list_formatter
        },

        { "include_actions": NIGHT_ACTIONS, "model": model_10_01, "paragraph_formatter": latex_unordered_list_formatter },
    # END PART 2
    # PART THE HOUSE/AGENCY 
    { "include_actions": AFTERNOON_ACTIONS + NIGHT_ACTIONS + OBSERVATION_ACTIONS, "model": model_1_06, "paragraph_formatter": latex_single_paragraph_formatter },
    { "include_actions": MORNING_ACTIONS + OBSERVATION_ACTIONS, "model": model_1_06, "paragraph_formatter": latex_single_paragraph_formatter },
    { 
        "include_actions": MORNING_ACTIONS + AGENCY_ACTIONS, 
        "model": model_1_05,
        "paragraph_formatter": latex_single_paragraph_formatter
    },

    { "include_actions": AFTERNOON_ACTIONS + NIGHT_ACTIONS + OBSERVATION_ACTIONS, "model": model_1_06, "paragraph_formatter": latex_single_paragraph_formatter },
    { "include_actions": SURVEILLANCE_ACTIONS + OBSERVATION_ACTIONS, "model": model_1_06, "paragraph_formatter": latex_single_paragraph_formatter },

    { "include_actions": NIGHT_ACTIONS, "model": model_1_11 },
    # END PART HOUSE/AGENCY #

    # PART SURVEILLANCE
    # OBSERVATION + NIGHT, number list
    { "include_actions": OBSERVATION_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    { "include_actions": OBSERVATION_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    # OBSERVATION + NIGHT, number list
    { "include_actions": OBSERVATION_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    { "include_actions": OBSERVATION_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    # AGENCY + NIGHT
    { "include_actions": AGENCY_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    { "include_actions": AGENCY_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    # MORNING + NIGHT
    { "include_actions": MORNING_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    { "include_actions": MORNING_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    # NIGHT
    { "include_actions": NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    { "include_actions": NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    # MORNING + AFTERNOON + AGENCY
    { "include_actions": MORNING_ACTIONS + AFTERNOON_ACTIONS + AGENCY_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    # OBSERVATION + NIGHT
    { "include_actions": OBSERVATION_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    { "include_actions": OBSERVATION_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    # OBSERVATION + NIGHT
    { "include_actions": OBSERVATION_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    { "include_actions": OBSERVATION_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    # OBSERVATION + NIGHT
    { "include_actions": OBSERVATION_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    { "include_actions": OBSERVATION_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    # OBSERVATION + NIGHT
    { "include_actions": OBSERVATION_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    { "include_actions": OBSERVATION_ACTIONS + NIGHT_ACTIONS, "model": model_1_07, "paragraph_formatter": latex_ordered_list_formatter },
    # PART 5 - THE MACHINE 
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": MACHINE_ACTIONS, "model": model_1_08 },
    { "include_actions": AFTERNOON_ACTIONS, "model": model_1_08 },
    { "include_actions": AFTERNOON_ACTIONS, "model": model_1_08 },
    { "include_actions": AFTERNOON_ACTIONS, "model": model_1_08 },
    { "include_actions": AFTERNOON_ACTIONS + NIGHT_ACTIONS, "model": model_1_08 },
    { "include_actions": AFTERNOON_ACTIONS + NIGHT_ACTIONS, "model": model_1_08 },
    { "include_actions": AFTERNOON_ACTIONS + NIGHT_ACTIONS, "model": model_1_08 },
    { "include_actions": NIGHT_ACTIONS, "model": model_1_08 },
    # END PART 5 #
    # PART 6  - REPORTS AND DEATH
    { "model": model_3_03, "paragraph_formatter": latex_single_paragraph_formatter, "section_formatter": latex_unordered_list_formatter },
    { "model": model_2_05, "paragraph_formatter": latex_single_paragraph_formatter, "section_formatter": latex_unordered_list_formatter },
    { "model": model_3_03, "paragraph_formatter": latex_single_paragraph_formatter, "section_formatter": latex_unordered_list_formatter },
    { "model": model_2_05, "paragraph_formatter": latex_single_paragraph_formatter, "section_formatter": latex_unordered_list_formatter },
    { "model": model_2_05, "paragraph_formatter": latex_single_paragraph_formatter, "section_formatter": latex_unordered_list_formatter },
    { "model": model_2_05, "paragraph_formatter": latex_single_paragraph_formatter, "section_formatter": latex_unordered_list_formatter },
    { "model": model_3_03, "paragraph_formatter": latex_single_paragraph_formatter, "section_formatter": latex_unordered_list_formatter },
    # END PART 6 #
    # PART 7 - OBSERVATIONS AND DEATH AND REFUSAL AND DREAMS
    { "include_actions": ['AGENT_WAKES'], "model": model_1_12 },
    { "include_actions": ['AGENT_WAKES'], "model": model_1_12 },
    { "include_actions": ['AGENT_WAKES'], "model": model_1_12 },
    { "include_actions": NIGHT_ACTIONS, "model": model_1_11 },
    { "include_actions": NIGHT_ACTIONS, "model": model_1_11 },
    { "include_actions": NIGHT_ACTIONS, "model": model_1_11 },
    { "include_actions": ['AGENT_WAKES'], "model": model_1_12 },
    { "include_actions": ['AGENT_WAKES'], "model": model_1_12 },
    { "include_actions": ['AGENT_WAKES'], "model": model_1_12 },
    { "include_actions": NIGHT_ACTIONS, "model": model_1_12 },
    # END PART 7 #

    ### FIN....?


]

latex_book_output_config = {
    "output_sink": latex_sink,
    "chapter_list_to_string": latex_new_page_formatter,
    "default_paragraph_formatter": latex_unordered_list_formatter,
    "default_section_formatter": latex_single_paragraph_formatter,
    "chapter_configs": chapter_configs
}

log_book_output_config = {
    "output_sink": log_sink,
    "chapter_list_to_string": new_page_formatter,
    "default_paragraph_formatter": unordered_list_formatter,
    "default_section_formatter": star_separator_formatter,
    "chapter_configs": chapter_configs
}

#default_book_output_config = log_book_output_config
default_book_output_config = latex_book_output_config 
