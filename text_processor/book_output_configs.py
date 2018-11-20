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

def output_stdout(input: str):
    """ Default is to print to stdout"""
    print(input)

default_book_output_config = {
    "output_fn": output_file,
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
