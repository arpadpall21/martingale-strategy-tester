"""
    Random Strategy:
      - On Win or Lose
          - Betting randomly while randomly changing the bet size
"""
from typing import Any
import random

from misc.rand_success import check_success
from misc.update_counters import update_counters, Counters
from misc.log import log, log_strategy_header, log_end_game


def random_bet(start_sum: int,
               success_chance_percent_each_cycle: int,
               cycles: int,
               log_verbose: bool,
               options: dict[str, Any] = {"bet_range": [1, 1]}) -> int:
    log_strategy_header("Random Bet", start_sum, success_chance_percent_each_cycle, cycles, log_verbose)

    current_sum: int = start_sum
    win_counters: Counters = Counters(0, 0, 0)
    lose_counters: Counters = Counters(0, 0, 0)

    for cycle in range(cycles):
        log(f"Cycle: {cycle + 1}", log_verbose)
        if check_success(success_chance_percent_each_cycle):
            update_counters("win", win_counters, lose_counters)
            current_bet = random.randint(options["bet_range"][0], options["bet_range"][1])
            current_sum += current_bet
            log(f"  Win -> current sum: {current_sum} (current bet={current_bet})", log_verbose)
        else:
            update_counters("lose", win_counters, lose_counters)
            planned_bet: int = random.randint(options["bet_range"][0], options["bet_range"][1])
            current_bet: int = planned_bet if planned_bet < current_sum else current_sum
            current_sum -= current_bet
            log(f"  Lose -> current sum: {current_sum} (current bet={current_bet})", log_verbose)

            if current_sum <= 0:
                log_end_game("You run out of cache", current_sum, win_counters, lose_counters, log_verbose)
                return current_sum

    log_end_game("End Game", current_sum, win_counters, lose_counters, True)
    return current_sum
