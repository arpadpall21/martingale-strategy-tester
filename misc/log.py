from misc.update_counters import Counters
from typing import Literal


def log(txt: str, show: bool):
    if show:
        print(txt)


def log_strategy_header(strategy_name: str,
                        start_sum: int,
                        success_chance_percent_each_cycle: float,
                        cycles: int,
                        log_verbose: bool) -> None:
    log(f"Stragety Name: {strategy_name}", log_verbose)
    log(f"Start Sum: {start_sum}", log_verbose)
    log(f"Success Chance Each Turn: {success_chance_percent_each_cycle}%", log_verbose)
    log(f"Planned Cycles: {cycles}\n", log_verbose)


def log_cycle_status(state: Literal["win", "lose"],
                     current_sum: int | float,
                     current_bet: int | float,
                     next_bet: int | float,
                     log_verbose: bool) -> None:
    if isinstance(current_sum, float):
        current_sum = round(current_sum, 2)
    if isinstance(current_bet, float):
        current_bet = round(current_bet, 2)
    if isinstance(next_bet, float):
        next_bet = round(next_bet, 2)

    log(
        f"  {state.capitalize()} -> current sum: {current_sum} (current bet={current_bet}) (next bet={next_bet})",
        log_verbose,
    )


def log_end_game(reason: str,
                 current_sum: int,
                 win_counters: Counters,
                 lose_counters: Counters,
                 log_verbose: bool) -> None:
    log(
        f"{reason} -> current sum: {current_sum} (win cycle count={win_counters.cycle}) " +
        f"(lose cycle count={lose_counters.cycle}) (max win streak count={win_counters.max_streak}) " +
        f"(max lose streak count={lose_counters.max_streak})",
        log_verbose
    )


def log_multi_game(base_config: dict[str, int | bool],
                   multi_game_cycles: int,
                   win_cycles: int,
                   loss_cycles: int,
                   balance: int | float,
                   ):
    initial_start_sum: int = base_config["start_sum"]
    total_start_sum: int = initial_start_sum * multi_game_cycles
    total_net_balance: int | float = balance - total_start_sum

    if isinstance(balance, float):
        balance = round(balance, 2)
    if isinstance(total_net_balance, float):
        total_net_balance = round(total_net_balance, 2)

    print(
        f"Multi Game Report: (nr of games played={multi_game_cycles})"
        f"(initial start sum={initial_start_sum}) (total start sum={total_start_sum})"
        f"(win cycles={win_cycles}) (loss cycles={loss_cycles}) " +
        f"(total sum at the end of games={balance}) (total net balance={total_net_balance}) " +
        f"(total balance ratio={round(balance / total_start_sum * 100, 1)}%)"
    )
