from misc.update_counters import Counters


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
