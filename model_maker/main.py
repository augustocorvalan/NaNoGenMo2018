from characters.AgentCharacter import Agent
from typing import Dict, List

def get_days(model: Agent, total_days: int) -> dict:
    days = []

    for i in range(total_days):
        if not model.has_killed():
            days.append(model.get_day())

    return {'days': days}

if __name__ == '__main__':
    model = get_days(model=Agent(), total_days=3)

    print(model)
