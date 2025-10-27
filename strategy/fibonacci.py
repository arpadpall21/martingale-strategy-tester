"""
    Standard Martingale Strategy:
        - On Win:
            - TODO...
        - On Lose:
            - TODO...
"""
from typing import Literal

from misc.rand_success import check_success
from misc.update_counters import update_counters, Counters
from misc.log import log, log_strategy_header, log_end_game


def fibonacci(start_sum: int,
              success_chance_percent_each_cycle: int,
              cycles: int,
              log_verbose: bool) -> int:
    log_strategy_header("Fibonachi", start_sum, success_chance_percent_each_cycle, cycles, log_verbose)

    return 0


def get_next_fibonacci(value: int, direction: Literal["next", "previous"] = 'next'):
    n1: int = 1
    n2: int = 1
    next_fib_val: int = n1 + n2
    while next_fib_val <= value:
        n1: int = n2
        n2 = next_fib_val
        next_fib_val = n1 + n2

    return next_fib_val if direction == "next" else n1

