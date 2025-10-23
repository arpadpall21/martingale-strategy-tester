"""
    Reverse Martingale Strategy:
        - On Win: 
            - TODO:...
        - On Lose: 
            - TODO:...
"""
from typing import Any

from misc.rand_success import check_success
from misc.update_counters import update_counters, Counters
from misc.log import log, log_strategy_header, log_end_game


def reverse_martingale(start_sum: int,
                       success_chance_percent_each_cycle: int,
                       cycles: int,
                       log_verbose: bool) -> int:
    log_strategy_header("Reverse Martingale", start_sum, success_chance_percent_each_cycle, cycles, log_verbose)

    current_sum: int = start_sum
    win_counters = Counters(0, 0, 0)
    lose_counters = Counters(0, 0, 0)

    log_end_game("End Game", current_sum, win_counters, lose_counters, log_verbose)
    return current_sum
