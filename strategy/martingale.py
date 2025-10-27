"""
    Standard Martingale Strategy:
        - On Win:
            - Bet the initial bet
        - On Lose:
            - Bet double the amount you recently lost
"""
from misc.rand_success import check_success
from misc.update_counters import update_counters, Counters
from misc.log import log, log_strategy_header, log_end_game


def martingale(start_sum: int,
               success_chance_percent_each_cycle: int,
               cycles: int,
               log_verbose: bool,
               options: dict[str, bool] = {"run_till_win": False}) -> int:
    log_strategy_header("Martingale", start_sum, success_chance_percent_each_cycle, cycles, log_verbose)

    current_sum: int = start_sum
    current_bet: int = 1
    win_counters: Counters = Counters(0, 0, 0)
    lose_counters: Counters = Counters(0, 0, 0)
    cycle_count: int = 1
    current_cycle_win: bool = False

    while cycle_count <= cycles or (options.get("run_till_win") and not current_cycle_win):
        log(f"Cycle: {cycle_count}", log_verbose)
        if check_success(success_chance_percent_each_cycle):
            update_counters("win", win_counters, lose_counters)
            current_sum += current_bet
            next_bet = 1
            log(f"  Win -> current sum: {current_sum} (current bet={current_bet}) (next bet={next_bet})", log_verbose)

            current_bet = next_bet
            current_cycle_win = True
        else:
            update_counters("lose", win_counters, lose_counters)
            current_sum -= current_bet if current_bet <= current_sum else current_sum
            next_bet = current_bet * 2 if current_bet * 2 < current_sum else current_sum
            log(f"  Lose -> current sum: {current_sum} (current bet={current_bet}) (next bet={next_bet})", log_verbose)

            if current_sum <= 0:
                log_end_game("You run out of cache", current_sum, win_counters, lose_counters, True)
                return current_sum

            current_bet = next_bet
            current_cycle_win = False
        cycle_count += 1

    log_end_game("End Game", current_sum, win_counters, lose_counters, True)
    return current_sum
