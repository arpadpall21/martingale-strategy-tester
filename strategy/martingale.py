from misc.rand_success import check_success


def martingale(start_sum: int, success_chance_percent_each_cycle: int, cycles: int) -> None:
    print("Stragety Name: Martingale")
    print(f"Start Sum: {start_sum}")
    print(f"Success Chance Percent Each Turn: {success_chance_percent_each_cycle}")
    print(f"Total Cycles: {cycles}\n")

    current_sum: int = start_sum

    for cycle in range(cycles):
        print(f"Cycle: {cycle + 1}")

    print(f"End Sum: {current_sum}")
