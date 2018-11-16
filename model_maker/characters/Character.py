from DayTicker import DayTicker

class Character(object):
    """ Default character model """

    def __init__(self, model): 
        self.day_ticker = DayTicker()
        self.model = model

    def get_day(self, config) -> list:
        day_ticker: DayTicker = self.day_ticker

        # model begins the day by waking up!
        self.model.wake_up()

        # while the day still has hours...
        while(day_ticker.has_next_tick()):
            # model takes next action (if any)
            self.model.next_action()
            # another tick of the clock has passed
            day_ticker.mark_next_tick()
        

        return [{ "action_name": action } for action in self.model.actions]