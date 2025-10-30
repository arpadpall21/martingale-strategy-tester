"""
    Random Strategy:
        - On Win
            - TODO...
        - On Lose
            - Bet multiplier times the amount you recently lost
"""
from misc.rand_success import check_success
from misc.update_counters import update_counters, Counters
from misc.log import log, log_strategy_header, log_cycle_status, log_end_game


def pyramide_martingale(start_sum: int,
                        success_chance_percent_each_cycle: int,
                        cycles: int,
                        log_verbose: bool,
                        percent_target: None | int = None,
                        options: dict[str, list[int]] = {"multiplier": 1.5}) -> int | float:
    log_strategy_header("Pyramide Martingale", start_sum, success_chance_percent_each_cycle, cycles, log_verbose)

    current_sum: int = start_sum
    target_sum: int = None if percent_target is None else start_sum + (start_sum / 100 * percent_target)
    current_bet: float = 1
    win_counters: Counters = Counters(0, 0, 0)
    lose_counters: Counters = Counters(0, 0, 0)

    for cycle in range(cycles):
        log(f"Cycle: {cycle + 1}", log_verbose)
        if check_success(success_chance_percent_each_cycle):
            update_counters("win", win_counters, lose_counters)
            current_sum += current_bet
            next_bet: float = 1

            log_cycle_status("win", current_sum, current_bet, next_bet, log_verbose)
            current_bet = next_bet
        else:
            update_counters("lose", win_counters, lose_counters)
            current_sum -= current_bet
            planned_next_bet: float = current_bet * options["multiplier"]
            next_bet: int = planned_next_bet if planned_next_bet < current_sum else current_sum

            log_cycle_status("lose", current_sum, current_bet, next_bet, log_verbose)
            current_bet = next_bet

        if current_sum <= 0:
            log_end_game("You run out of cache", current_sum, win_counters, lose_counters, True)
            return current_sum
        if target_sum and current_sum >= target_sum:
            log_end_game("Target Reached", current_sum, win_counters, lose_counters, True)
            return current_sum

    log_end_game("End Game", current_sum, win_counters, lose_counters, True)
    return current_sum
