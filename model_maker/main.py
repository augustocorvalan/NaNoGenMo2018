from characters.AgentCharacter import Agent 
from characters.Character import Character
from typing import Dict, List


def get_model(model_config: dict) -> dict:
    return {
        "days": get_days(model_config)
    }

def get_days(model_config: dict) -> list:
    total_days: int = model_config['total_days']
    days = []

    for i in range(total_days):
        day: dict = get_day(model_config)
        days.append(day)

    return days


def get_day(model_config) -> dict:
    characters: List[dict] = model_config['characters']
    day = {}

    for character in characters:
        character_name = character['name']
        character_controller = character['controller']
        character_day: list = character_controller.get_day(model_config) 

        day[character_name] = character_day

    return day






## CONFIG
default_model_config = {
    "characters":  [
        {"name": 'agent', "controller": Character(Agent())}
    ],
    "total_days": 3
}
## CONFIG
model = get_model(default_model_config)

print(model)


########################################


