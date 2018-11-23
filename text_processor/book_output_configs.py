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
def terminal_sink(input: str):
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
    content = r'''
    %s
    \bigskip
    '''

    return ''.join(content%item for item in lst)


def new_page_formatter(lst: list) -> str:
    content = r'''
    %s
    \newpage
    '''

    return ''.join(content%item for item in lst)

def latex_new_page_formatter(lst: list) -> str:
    return '\newpage%'.join(lst)

def latex_unordered_list_formatter(lst: list) -> str:
    return '\\ \\'.join(lst)


alt_config = {
    "output_sink": latex_sink,
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
default_book_output_config = {
    "output_sink": latex_sink,
    "chapter_list_to_string": new_page_formatter,
    "default_paragraph_formatter": unordered_list_formatter,
    "default_section_formatter": star_separator_formatter,
    "chapter_configs": [
        { "config": MorningConfig, "model": model_1_01 },
        { "config": MorningConfig, "model": model_1_02 },
        { "config": MorningConfig, "model": model_1_02 },
        # TODO morning + night
        # TODO machine description
        # TODO morning + night
        # TODO machine description
        # TODO machine description (funky formatter)

    ]
}
