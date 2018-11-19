import random

# from transitions import Machine
from transitions.extensions import LockedHierarchicalGraphMachine as Machine

from DayTicker import DayTicker

class Agent(object):
    #remembering the agency
    #agent dreams/nightmare
    #examines weapon (only nightmare machine)
    #agent questions mission
    #agent_pos_interaction
    #agent_neg_interaction
    #eat
    #exercise
    #report (to agency)
    #break_from_reality (action: break)
    #agent finds surveillance device
    states = [
        'awake',
        'asleep',
        'observing',
        'using_bathroom',
        'killing',
        'remembering',
        'dreams',
        'nightmares',
        'examine_weapon',
        'doubts',
        'pos_interaction_rev',
        'neg_interaction_rev',
        'eat',
        'exercise',
        'report',
        'break',
        'receive_direction',
        'discover_surveillance'
    ]

    transitions = [
        { 'trigger': 'wake_up', 'source': ['asleep', 'dreams', 'nightmares'], 'dest': 'awake'},
        # { 'trigger': 'next_action', 'source': 'awake', 'dest': 'using_bathroom', 'conditions': ['is_dirty']},
        { 'trigger': 'next_action', 'source': 'awake', 'dest': 'observing', 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'source': ['observing', 'using_bathroom'], 'dest': 'killing', 'conditions': ['wants_to_kill']},
        { 'trigger': 'next_action', 'dest': 'remembering', 'source': ['receive_direction', 'using_bathroom', 'examine_weapon', 'doubts'], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'dreams', 'source': ['asleep'], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'nightmares', 'source': ['asleep'], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'examine_weapon', 'source': ['remembering', 'receive_direction', 'break'], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'doubts', 'source': ['receive_direction', 'pos_interaction_rev'], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'pos_interaction_rev', 'source': ['observing', 'using_bathroom', 'dreams'], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'neg_interaction_rev', 'source': ['examine_weapon', 'nightmares', 'receive_direction'], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'eat', 'source': ['observing', 'using_bathroom'], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'exercise', 'source': ['observing', 'using_bathroom', 'pos_interaction_rev'], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'report', 'source': ['observing', 'neg_interaction_rev', ''], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'break', 'source': ['discover_surveillance', 'using_bathroom'], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'receive_direction', 'source': ['observing', 'using_bathroom', 'report'], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'discover_surveillance', 'source': ['exercise', 'break'], 'conditions': ['fifty_p']},
        { 'trigger': 'next_action', 'dest': 'asleep', 'source': ['observing', 'using_bathroom', 'eat'], 'conditions': ['fifty_p']},
    ]

    actions_dict = {
        "AGENT_WAKES":"AGENT_WAKES",
        "AGENT_OBSERVES_SELF":"AGENT_OBSERVES_SELF",
        "AGENT_SLEEPS":"AGENT_SLEEPS",
        "AGENT_USES_BATHROOM": "AGENT_USES_BATHROOM",
        "AGENT_KILLS_REV":"AGENT_KILLS_REV"
    }

    hygiene = random.randint(1, 5)
    hygiene_tolerance = 3
    max_hygiene = 5

    def __init__(self):
        # keep track of actions
        self.actions = []

        # make the machine
        self.machine = Machine(model=self, transitions=self.transitions, states=self.states, initial='asleep', ignore_invalid_triggers=True)
        self.day_ticker = DayTicker()

    def get_day(self) -> list:
        day_ticker: DayTicker = self.day_ticker

        # model begins the day by waking up!
        self.wake_up()

        # while the day still has hours...
        while(day_ticker.has_next_tick()):
            # model takes next action (if any)
            self.next_action()
            # another tick of the clock has passed
            day_ticker.mark_next_tick()

        day_ticker.current_time = 0
        # we need to reset day_ticker to run again
        # need to reset the actions (or get all the actions for all the days)
        return [{ "action_name": action } for action in self.actions]

    def add_action(self, action_name: str):
        self.actions.append((action_name))

    def has_taken_action(self, action_name: str) -> bool:
        return action_name in self.actions

    def is_dirty(self) -> bool:
        """ Agent is dirty hygiene is lower than tolerance """
        return self.hygiene < self.hygiene_tolerance

    def gets_clean(self):
        """ max hygiene! """
        self.hygiene = self.max_hygiene

    def fifty_p(self) -> bool:
        """ flip of a coin for the moment """
        return random.random() < 0.2

    def has_killed(self) -> bool:
        return self.has_taken_action(self.actions_dict['AGENT_KILLS_REV'])

    def wants_to_kill(self) -> bool:
        """ Only if the agent hasn't killed and flip of a coin """
        return random.random() < 0.5

    def on_enter_awake(self):
        self.add_action(self.actions_dict['AGENT_WAKES'])

    def on_enter_observing(self):
        self.add_action(self.actions_dict['AGENT_OBSERVES_SELF'])

    def on_enter_using_bathroom(self):
        # going to the bathroom makes you clean!
        self.gets_clean()
        self.add_action(self.actions_dict['AGENT_USES_BATHROOM'])

    def on_enter_killing(self):
        self.add_action(self.actions_dict['AGENT_KILLS_REV'])

    def on_enter_asleep(self):
        self.add_action(self.actions_dict['AGENT_SLEEPS'])
