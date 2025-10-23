from dataclasses import dataclass

@dataclass
class Counters():
    cycle: int
    max_streak: int
    current_straik: int


def update_counters(counters: Counters) -> None:
    pass
