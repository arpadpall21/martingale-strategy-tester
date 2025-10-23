"""
    Random Strategy:
      - betting randomly while randomly changing the bet size
"""
from typing import Any
import random

from misc.rand_success import check_success
from misc.streak_counter import update_counters, Counters
from misc.log import log, log_strategy_header


def random_bet(start_sum: int,
               success_chance_percent_each_cycle: int,
               cycles: int,
               log_verbose: bool,
               options: dict[str, Any] = {"bet_range": [1, 1]}) -> int:
    log_strategy_header("Random Bet", start_sum, success_chance_percent_each_cycle, cycles, log_verbose)

    current_sum: int = start_sum
    win_counters = Counters(0, 0, 0)
    lose_counters = Counters(0, 0, 0)
    cycle_count: int = 1

    for cycle in range(cycles):
        log(f"Cycle: {cycle_count}", log_verbose)
        if check_success(success_chance_percent_each_cycle):
            update_counters("win", win_counters, lose_counters)
            current_bet = random.randint(options["bet_range"][0], options["bet_range"][0])
            current_sum += current_bet
            log(f"  Win -> current sum: {current_sum} (current bet={current_bet})", log_verbose)
        else:
            update_counters("lose", win_counters, lose_counters)
            planned_bet: int = random.randint(options["bet_range"][0], options["bet_range"][0])
            current_bet: int = planned_bet if planned_bet < current_sum else current_sum
            current_sum -= current_bet
            log(f"  Lose -> current sum: {current_sum} (current bet={current_bet})", log_verbose)

            if current_sum <= 0:
                log(
                    f"You run out of cache -> current sum: {current_sum} (win cycle count={win_counters.cycle}) " +
                    f"(lose cycle count={lose_counters.cycle}) (max win streak count={win_counters.max_streak}) " +
                    f"(max lose streak count={lose_counters.max_streak})",
                    True
                )
                return current_sum

    log(
        f"End sum: {current_sum} (win cycle count={win_counters.cycle}) (lose cycle count={lose_counters.cycle}) " +
        f"(max win streak count={win_counters.max_streak}) (max lose streak count={lose_counters.max_streak})",
        True
    )
    return current_sum
