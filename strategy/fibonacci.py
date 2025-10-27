"""
    Standard Martingale Strategy:
        - On Win:
            - TODO...
        - On Lose:
            - TODO...
"""
from typing import Literal

from misc.rand_success import check_success
from misc.update_counters import update_counters, Counters
from misc.log import log, log_strategy_header, log_end_game


def fibonacci(start_sum: int,
              success_chance_percent_each_cycle: int,
              cycles: int,
              log_verbose: bool) -> int:
    log_strategy_header("Fibonacci", start_sum, success_chance_percent_each_cycle, cycles, log_verbose)

    current_sum: int = start_sum
    current_bet: int = 1
    win_counters: Counters = Counters(0, 0, 0)
    lose_counters: Counters = Counters(0, 0, 0)

    for cycle in range(cycles):
        log(f"Cycle: {cycle + 1}", log_verbose)
        if check_success(success_chance_percent_each_cycle):
            update_counters("win", win_counters, lose_counters)
            current_sum += current_bet
            next_bet: int = get_next_fibonacci_val(get_next_fibonacci_val(current_bet, "previous"), "previous")
            log(f"  Win -> current sum: {current_sum} (current bet={current_bet}) (next bet={next_bet})", log_verbose)

            current_bet = next_bet
        else:
            update_counters("lose", win_counters, lose_counters)
            current_sum -= current_bet
            planned_next_bet: int = get_next_fibonacci_val(current_bet, "next")
            next_bet: int = planned_next_bet if planned_next_bet < current_sum else current_sum
            log(f"  Lose -> current sum: {current_sum} (current bet={current_bet}) (next bet={next_bet})", log_verbose)

            current_bet = next_bet
            if current_sum <= 0:
                log_end_game("You run out of cache", current_sum, win_counters, lose_counters, log_verbose)
                return current_sum

    log_end_game("End Game", current_sum, win_counters, lose_counters, True)
    return current_sum


def get_next_fibonacci_val(value: int, direction: Literal["next", "previous"] = "next"):
    n1: int = 1
    n2: int = 1
    next_fib_val: int = n1 + n2

    while next_fib_val <= value:
        n1: int = n2
        n2 = next_fib_val
        next_fib_val = n1 + n2

    return next_fib_val if direction == "next" else n1




'''
1       
2       3
3       6
5       11
8       19 - 13      6
13      32
21      53 - 34      19
34      
55      
89      
144     
233     
377     
610     
987     
1597    
2584    
4181    
'''