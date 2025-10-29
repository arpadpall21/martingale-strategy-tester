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


def log_cycle_status(state: Literal["Win", "Lose"],
                     current_sum: int,
                     current_bet: int,
                     next_bet: int,
                     log_verbose: bool) -> None:
    log(f"  {state} -> current sum: {current_sum} (current bet={current_bet}) (next bet={next_bet})", log_verbose)


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
                   balance: int,
                   ):
    initial_start_sum: int = base_config["start_sum"]
    total_start_sum: int = initial_start_sum * multi_game_cycles

    print(
        f"Multi Game Report: (nr of games played={multi_game_cycles})"
        f"(initial start sum={initial_start_sum}) (total start sum={total_start_sum})"
        f"(win cycles={win_cycles}) (loss cycles={loss_cycles}) " +
        f"(total sum at the end of games={balance}) (total net balance={balance - total_start_sum}) " +
        f"(total balance ratio={round(balance / total_start_sum * 100, 1)}%)"
    )
