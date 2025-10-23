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
