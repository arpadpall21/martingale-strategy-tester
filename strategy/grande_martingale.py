"""
    Grande Martingale Strategy:
        - On Win:
            - Bet the initial bet
        - On Lose:
            - Bet double the amount you recently lost + extra bet (configurable (Default: 1))
"""
from misc.rand_success import check_success
from misc.update_counters import update_counters, Counters
from misc.log import log, log_strategy_header, log_end_game


def grande_martingale(start_sum: int,
                      success_chance_percent_each_cycle: int,
                      cycles: int,
                      log_verbose: bool,
                      options: dict[str, bool] = {"run_till_win": False, "extra_bet": 1}) -> int:
    log_strategy_header("Grande Martingale", start_sum, success_chance_percent_each_cycle, cycles, log_verbose)

    return 0
