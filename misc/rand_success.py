import random


def check_success(success_chance_percent: float = 50) -> bool:
    if success_chance_percent >= round(random.uniform(1, 100), 2):
        return True
    return False
