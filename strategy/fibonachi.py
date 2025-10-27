"""
    Standard Martingale Strategy:
        - On Win:
            - TODO...
        - On Lose:
            - TODO...
"""
from misc.rand_success import check_success
from misc.update_counters import update_counters, Counters
from misc.log import log, log_strategy_header, log_end_game


def fibonachi(start_sum: int,
              success_chance_percent_each_cycle: int,
              cycles: int,
              log_verbose: bool) -> int:
    log_strategy_header("Fibonachi", start_sum, success_chance_percent_each_cycle, cycles, log_verbose)

    return 0
