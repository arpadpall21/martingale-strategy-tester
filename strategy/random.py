"""
    Random Strategy:
      - betting randomly while randomly changing the bet size
"""
from typing import Any

from misc.rand_success import check_success
from misc.streak_counter import update_counters, Counters
from misc.log import log, log_strategy_header


def random(start_sum: int,
           success_chance_percent_each_cycle: int,
           cycles: int,
           log_verbose: bool,
           options: dict[str, Any] = {"bet_range": [1, 1]}) -> int:
    log_strategy_header("Random", start_sum, success_chance_percent_each_cycle, cycles, log_verbose)

    return 0
