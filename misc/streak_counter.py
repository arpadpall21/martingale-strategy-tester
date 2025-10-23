from dataclasses import dataclass
from typing import Literal


@dataclass
class Counters():
    cycle: int
    max_streak: int
    current_straik: int


def update_counters(status: Literal["win", "lose"], win_counters: Counters, lose_counters: Counters) -> None:
    if status == "win":
        win_counters.cycle += 1
        win_counters.current_straik += 1
        win_counters.max_streak = (
            win_counters.current_straik
            if win_counters.current_straik > win_counters.max_streak
            else win_counters.max_streak
        )
        lose_counters.current_straik = 0
    elif status == "lose":
        lose_counters.cycle += 1
        lose_counters.current_straik += 1
        lose_counters.max_streak = (
            lose_counters.current_straik
            if lose_counters.current_straik > lose_counters.max_streak
            else lose_counters.max_streak
        )
        win_counters.current_straik = 0
