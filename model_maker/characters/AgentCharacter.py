from characters.Character import Character
from DayTicker import DayTicker
from actions.agent_actions import actions

from transitions import Machine
import random

class Agent(object):
    states = ['awake', 'asleep', 'observing', 'using_bathroom', 'killing']

    hygiene = random.randint(1, 5)
    hygiene_tolerance = 3
    max_hygiene = 5

    def __init__(self):
        # keep track of actions
        self.actions = []

        # make the machine
        self.machine = Machine(model=self, states=Agent.states, initial='asleep', ignore_invalid_triggers=True)

        # Transitions
        # agent wants to wake up after sleeping
        self.machine.add_transition(trigger='wake_up', source='asleep', dest='awake')

        # agent wants to use the bathroom after waking, only if they're dirty!
        self.machine.add_transition(trigger='next_action', source='awake', dest='using_bathroom', conditions=['is_dirty'])
        self.machine.add_transition(trigger='next_action', source='awake', dest='observing', conditions=['is_thoughtful'])

        # after the agent uses the bathroom or observes he's tired. He either goes to sleep or finishes the job
        self.machine.add_transition(trigger='next_action', source=['observing', 'using_bathroom'], dest='killing', conditions=['wants_to_kill'])
        self.machine.add_transition(trigger='next_action', source=['observing', 'using_bathroom'], dest='asleep')


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

    def is_thoughtful(self) -> bool:
        """ flip of a coin for the moment """
        return random.random() < 0.5

    def has_killed(self) -> bool:
        return self.has_taken_action(actions['AGENT_KILLS_REV']) 
    def wants_to_kill(self) -> bool:
        """ Only if the agent hasn't killed and flip of a coin """
        return not self.has_killed() and random.random() < 0.5


    def on_enter_awake(self): 
        self.add_action(actions['AGENT_WAKES'])
    def on_enter_observing(self): 
        self.add_action(actions['AGENT_OBSERVES_SELF'])
    def on_enter_using_bathroom(self): 
        # going to the bathroom makes you clean!
        self.gets_clean()
        self.add_action(actions['AGENT_USES_BATHROOM'])
    def on_enter_killing(self):
        self.add_action(actions['AGENT_KILLS_REV'])
    def on_enter_asleep(self):
        self.add_action(actions['AGENT_SLEEPS'])

