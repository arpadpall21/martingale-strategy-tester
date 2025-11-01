"""
    Standard Martingale Strategy:
        - On Win:
            - bet 2nd previous fiboncacci value
        - On Lose:
            - bet next fibonacci value
"""
from typing import Literal

from misc.rand_success import check_success
from misc.update_counters import update_counters, Counters
from misc.log import log, log_strategy_header, log_cycle_status, log_end_game


def fibonacci(start_sum: int,
              success_chance_percent_each_cycle: int,
              cycles: int,
              log_verbose: bool,
              percent_target: None | int = None) -> int:
    log_strategy_header("Fibonacci", start_sum, success_chance_percent_each_cycle, cycles, log_verbose)

    current_sum: int = start_sum
    target_sum: int = None if percent_target is None else start_sum + (start_sum / 100 * percent_target)
    current_bet: int = 1
    win_counters: Counters = Counters(0, 0, 0)
    lose_counters: Counters = Counters(0, 0, 0)

    for cycle in range(cycles):
        log(f"Cycle: {cycle + 1}", log_verbose)
        if check_success(success_chance_percent_each_cycle):
            update_counters("win", win_counters, lose_counters)
            current_sum += current_bet
            next_bet: int = _get_next_fibonacci_val(_get_next_fibonacci_val(current_bet, "previous"), "previous")

            log_cycle_status("win", current_sum, current_bet, next_bet, log_verbose)
            current_bet = next_bet
        else:
            update_counters("lose", win_counters, lose_counters)
            current_sum -= current_bet
            planned_next_bet: int = _get_next_fibonacci_val(current_bet, "next")
            next_bet: int = planned_next_bet if planned_next_bet < current_sum else current_sum

            log_cycle_status("lose", current_sum, current_bet, next_bet, log_verbose)
            current_bet = next_bet

        if current_sum <= 0:
            log_end_game("You run out of cache", current_sum, win_counters, lose_counters, "red", True)
            return current_sum
        if target_sum and current_sum >= target_sum:
            log_end_game("Target Reached", current_sum, win_counters, lose_counters, "green", True)
            return current_sum

    log_end_game("End Game", current_sum, win_counters, lose_counters, "yellow", True)
    return current_sum


def _get_next_fibonacci_val(value: int, direction: Literal["next", "previous"] = "next"):
    n1: int = 1
    n2: int = 1
    next_fib_val: int = n1 + n2

    while next_fib_val <= value:
        n1 = n2
        n2 = next_fib_val
        next_fib_val = n1 + n2

    return next_fib_val if direction == "next" else n1
