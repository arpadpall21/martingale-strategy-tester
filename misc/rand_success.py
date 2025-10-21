import random


def check_success(success_chance_percent: int = 50) -> bool:
    if success_chance_percent >= random.randint(1, 100):
        return True
    return False
