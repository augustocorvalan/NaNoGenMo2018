import random
import collections

# from transitions import Machine
#from transitions.extensions import LockedHierarchicalGraphMachine as Machine
from transitions import Machine

from DayTicker import DayTicker

class Agent(object):

    neg_states = [
        'AGENT_DISCOVERS_SURVEILLANCE',
    ]

    states = neg_states + [
        'AGENT_WAKES',

        'AGENT_OBSERVES_SELF',
        'AGENT_USES_BATHROOM',

        'AGENT_WRITES_REPORT',
        'AGENT_RECEIVES_DIRECTION',

        'AGENT_EATS',
        'AGENT_EXERCISES',

        'AGENT_SLEEPS',
        'AGENT_DREAMS',

        'remembering',
        'examine_weapon',
        'doubts',
        'pos_interaction_rev',
        'neg_interaction_rev',
        'break',
        'AGENT_KILLS_REV',
        'AGENT_NIGHTMARES'
    ]

    transitions = [
        { 'trigger': 'wake_up', 'source': '*', 'dest': 'AGENT_WAKES'},
        ### after waking up the agent wants to clean himself if they're dirty
        { 'trigger': 'next_action', 'source': 'AGENT_WAKES', 'dest': 'AGENT_USES_BATHROOM', 'conditions': ['is_dirty']},
        ### if he's ont dirty he may want to observe himself if they're feelingn thoughtful
        { 'trigger': 'next_action', 'source': 'AGENT_WAKES', 'dest': 'AGENT_OBSERVES_SELF', 'conditions': ['feels_thoughtful']},
        ### he should prolly do something agency related after taking care of the morning stuff
        { 'trigger': 'next_action', 'source': neg_states + ['AGENT_OBSERVES_SELF', 'AGENT_USES_BATHROOM'], 'dest': 'AGENT_WRITES_REPORT', 'conditions': ['coin_flip']},
        { 'trigger': 'next_action', 'source': neg_states + ['AGENT_OBSERVES_SELF', 'AGENT_USES_BATHROOM'], 'dest': 'AGENT_RECEIVES_DIRECTION', 'conditions': ['coin_flip']},
        ### what else does they do? eat, exercise
        { 'trigger': 'next_action', 'dest': 'AGENT_EATS', 'source': neg_states + ['AGENT_WRITES_REPORT', 'AGENT_RECEIVES_DIRECTION', 'AGENT_EXERCISES'], 'conditions': ['coin_flip', 'is_hungry']},
        { 'trigger': 'next_action', 'dest': 'AGENT_EXERCISES', 'source': neg_states + ['AGENT_WRITES_REPORT', 'AGENT_RECEIVES_DIRECTION', 'AGENT_EATS'], 'conditions': ['coin_flip'], 'unless': 'has_exercised'},
        # { 'trigger': 'next_action', 'dest': 'exercise', 'source': ['observing', 'using_bathroom', 'pos_interaction_rev'], 'conditions': ['fifty_p']},

        ### sweet sleep
        { 'trigger': 'next_action', 'dest': 'AGENT_SLEEPS', 'source': ['AGENT_EATS', 'AGENT_EXERCISES', 'AGENT_DISCOVERS_SURVEILLANCE'], 'conditions': ['coin_flip']},
        { 'trigger': 'next_action', 'dest': 'AGENT_DREAMS', 'source': ['AGENT_SLEEPS'], 'conditions': ['coin_flip']},

        ### at any point during the day the agent has a chance to discover surveillance device
        { 'trigger': 'next_action', 'dest': 'AGENT_DISCOVERS_SURVEILLANCE', 'source': '*', 'conditions': ['will_neg_event_happen']},


        # certain triggers will make the agent remember his past in the agency
        # { 'trigger': 'next_action', 'dest': 'remembering', 'source': ['receive_direction', 'using_bathroom', 'examine_weapon', 'doubts'], 'conditions': ['feels_thoughtful']},
        # { 'trigger': 'next_action', 'dest': 'examine_weapon', 'source': ['remembering', 'receive_direction', 'break'], 'conditions': ['fifty_p']},
        # { 'trigger': 'next_action', 'dest': 'doubts', 'source': ['receive_direction', 'pos_interaction_rev'], 'conditions': ['fifty_p']},
        # { 'trigger': 'next_action', 'dest': 'pos_interaction_rev', 'source': ['observing', 'using_bathroom', 'dreams'], 'conditions': ['fifty_p']},
        # { 'trigger': 'next_action', 'dest': 'neg_interaction_rev', 'source': ['examine_weapon', 'nightmares', 'receive_direction'], 'conditions': ['fifty_p']},
        # { 'trigger': 'next_action', 'dest': 'report', 'source': ['observing', 'neg_interaction_rev', ''], 'conditions': ['fifty_p']},
        # { 'trigger': 'next_action', 'dest': 'break', 'source': ['discover_surveillance', 'using_bathroom'], 'conditions': ['fifty_p']},
        # { 'trigger': 'next_action', 'dest': 'receive_direction', 'source': ['observing', 'using_bathroom', 'report'], 'conditions': ['fifty_p']},
        # { 'trigger': 'next_action', 'dest': 'discover_surveillance', 'source': ['exercise', 'break'], 'conditions': ['fifty_p']},


        # { 'trigger': 'next_action', 'dest': 'asleep', 'source': ['observing', 'using_bathroom', 'eat'], 'conditions': ['fifty_p']},

        # { 'trigger': 'next_action', 'source': ['observing', 'using_bathroom'], 'dest': 'killing', 'conditions': ['wants_to_kill']},

        # { 'trigger': 'next_action', 'dest': 'nightmares', 'source': ['asleep'], 'conditions': ['fifty_p']},
    ]

    # HYGIENE STUFF
    hygiene = random.randint(1, 5)
    hygiene_tolerance = 3
    max_hygiene = 5

    # EATING STUFF
    appetite = random.randint(1,2)
    meals_eaten = 0

    def __init__(self):
        # keep track of actions
        self.actions = []

        # make the machine
        self.machine = Machine(model=self, transitions=self.transitions, states=self.states, initial='asleep', ignore_invalid_triggers=True)
        # log all the actions this model takes
        self.machine.after_state_change = self.add_action

    def get_day(self) -> list:
        # new day equals new ticker
        day_ticker: DayTicker = DayTicker()
        # need to reset the actions
        self.actions = []

        # model begins the day by waking up!
        self.wake_up()

        # while the day still has hours...
        while(day_ticker.has_next_tick()):
            # model takes next action (if any)
            if (not self.state == 'AGENT_DREAMS' and not self.state == 'AGENT_SLEEPS'):
                self.next_action()
            # another tick of the clock has passed
            day_ticker.mark_next_tick()

        return [{ "action_name": action } for action in self.actions]

    # ACTION HELPERS
    def add_action(self):
        self.actions.append(self.state)
    def has_taken_action(self, action_name: str) -> bool:
        return action_name in self.actions

    # CONDITIONS
    def coin_flip(self) -> bool:
        return random.random() < 0.5
    def feels_thoughtful(self) -> bool:
        """ flip of a coin for the moment """
        return random.random() < 0.5
    def is_dirty(self) -> bool:
        """ Agent is dirty hygiene is lower than tolerance """
        return self.hygiene < self.hygiene_tolerance
    def has_exercised(self) -> bool:
        return self.has_taken_action('AGENT_EXERCISES')
    def is_hungry(self) -> bool:
        """ Agent is hungry if he hasn't eaten enough meals """
        return self.appetite > self.meals_eaten
    def will_neg_event_happen(self) -> bool:
        """ Currently, 1/5 chance """
        has_neg_event_happened = any(self.has_taken_action(action) for action in self.neg_states)
        #has_neg_event_happened = neg_events.any(self.has_taken_action)
        return not has_neg_event_happened and random.random() > 0.2 # TODO make this based on past events

    # HYGIENCE STUFF
    def gets_clean(self):
        """ max hygiene! """
        self.hygiene = self.max_hygiene

    def wants_to_kill(self) -> bool:
        """ Only if the agent hasn't killed and flip of a coin """
        return random.random() < 0.5

    def on_enter_AGENT_EATS(self):
        self.meals_eaten += 1
    def on_enter_using_bathroom(self):
        """ going to the bathroom makes you clean! """
        self.gets_clean()
