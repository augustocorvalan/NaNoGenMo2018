class DayTicker:
    current_time = 0
    end_time = 24
    time_interval = 1

    wake_time = 9
    sleep_time = 12

    def has_next_tick(self) -> bool:
        return self.current_time < self.end_time

    def mark_next_tick(self) -> int:
        self.current_time += self.time_interval

        return self.current_time

    