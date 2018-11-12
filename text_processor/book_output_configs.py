from chapter_configs.default_config import Config
from chapter_configs.morning_routine import MorningConfig

def output_stdout(input: str):
    """ Default is to print to stdout"""
    print(input)

default_book_output_config = {
    "output_fn": output_stdout,
    "chapter_configs": [  
        { "config": MorningConfig },
        { "config": Config },
        { "config": MorningConfig }
    ]
}
