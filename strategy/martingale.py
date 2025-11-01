"""
    Standard Martingale Strategy:
        - On Win:
            - Bet the initial bet
        - On Lose:
            - Bet double the amount you recently lost
"""
from misc.rand_success import check_success
from misc.update_counters import update_counters, Counters
from misc.log import log, log_strategy_header, log_cycle_status, log_end_game


def martingale(start_sum: int,
               success_chance_percent_each_cycle: int,
               cycles: int,
               log_verbose: bool = False,
               percent_target: None | int = None) -> int:
    log_strategy_header("Martingale", start_sum, success_chance_percent_each_cycle, cycles, log_verbose)

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
            next_bet = 1

            log_cycle_status("win", current_sum, current_bet, next_bet, log_verbose)
            current_bet = next_bet
        else:
            update_counters("lose", win_counters, lose_counters)
            current_sum -= current_bet if current_bet <= current_sum else current_sum
            next_bet = current_bet * 2 if current_bet * 2 < current_sum else current_sum

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
