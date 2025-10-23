"""
    Standard martinage strategy:
      - on win bet the initial bet
      - on lose bet double that you recently lost
"""

from misc.rand_success import check_success
from misc.streak_counter import update_counters, Counters
from misc.log import log


def martingale(start_sum: int, success_chance_percent_each_cycle: int, cycles: int, log_verbose: bool) -> int:
    log("Stragety Name: Martingale", log_verbose)
    log(f"Start Sum: {start_sum}", log_verbose)
    log(f"Success Chance Each Turn: {success_chance_percent_each_cycle}%", log_verbose)
    log(f"Planned Cycles: {cycles}\n", log_verbose)

    current_sum: int = start_sum
    current_bet: int = 1
    win_counters = Counters(0, 0, 0)
    lose_counters = Counters(0, 0, 0)
    cycle_count: int = 1
    current_cycle_win: bool = False

    while cycle_count <= 100 or not current_cycle_win:
        log(f"Cycle: {cycle_count}", log_verbose)
        if check_success(success_chance_percent_each_cycle):
            update_counters("win", win_counters, lose_counters)
            current_sum += current_bet
            log(f"  Win -> current sum: {current_sum} (current bet={current_bet}) (next bet={1})", log_verbose)

            current_bet = 1
            current_cycle_win = True
        else:
            update_counters("lose", win_counters, lose_counters)
            current_sum -= current_bet if current_bet <= current_sum else current_sum
            next_bet = current_bet * 2 if current_bet * 2 < current_sum else current_sum
            log(f"  Lose -> current sum: {current_sum} (current bet={current_bet}) (next bet={next_bet})", log_verbose)

            if current_sum <= 0:
                log(
                    f"You run out of cache -> current sum: {current_sum} (win cycle count={win_counters.cycle}) " +
                    f"(lose cycle count={lose_counters.cycle}) (max win streak count={win_counters.max_streak}) " +
                    f"(max lose streak count={lose_counters.max_streak})",
                    True
                )
                return current_sum

            current_bet = next_bet
            current_cycle_win = False
        cycle_count += 1

    log(
        f"End sum: {current_sum} (win cycle count={win_counters.cycle}) (lose cycle count={lose_counters.cycle}) " +
        f"(max win streak count={win_counters.max_streak}) (max lose streak count={lose_counters.max_streak})",
        True
    )
    return current_sum
