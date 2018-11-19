from chapter_configs.default_config import Config
from chapter_configs.morning_routine import MorningConfig

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
        { "config": MorningConfig },
        { "config": Config },
    ]
}
