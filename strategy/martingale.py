"""
    Standard martinage strategy:
      - on win bet the initial bet
      - on lose bet double that you recently lost
"""

from misc.rand_success import check_success
from misc.streak_counter import update_counters, Counters


def martingale(start_sum: int, success_chance_percent_each_cycle: int, cycles: int, exit_on_empty_balance: bool) -> int:
    print("Stragety Name: Martingale")
    print(f"Start Sum: {start_sum}")
    print(f"Success Chance Percent Each Turn: {success_chance_percent_each_cycle}")
    print(f"Planned Cycles: {cycles}\n")

    current_sum: int = start_sum
    current_bet: int = 1
    win_counters = Counters(0, 0, 0)
    lose_counters = Counters(0, 0, 0)

    for cycle in range(cycles):
        print(f"Cycle: {cycle + 1}")
        if check_success(success_chance_percent_each_cycle):
            update_counters(win_counters)
            current_sum += current_bet

            current_bet = 1
            print(f"  Win -> current sum: {current_sum}")

        else:
            update_counters(lose_counters)
            current_sum -= current_bet if current_bet <= current_sum else current_sum

            if exit_on_empty_balance and current_sum <= 0:
                print(
                    f"You run out of cache -> current sum: {current_sum} (win cycle count={win_counters.cycle}) " +
                    f"(lose cycle count={lose_counters.cycle}) (max win streak count={win_counters.max_streak}) " +
                    f"(max lose streak count={lose_counters.max_streak})"
                )
                return current_sum

            current_bet = current_bet * 2
            print(f"  Lose -> current sum: {current_sum}")

    print(
        f"End sum: {current_sum} (win cycle count={win_counters.cycle}) (lose cycle count={lose_counters.cycle}) " +
        f"(max win streak count={win_counters.max_streak}) (max lose streak count={lose_counters.max_streak})"
    )
    return current_sum
