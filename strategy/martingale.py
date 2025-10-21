from misc.rand_success import check_success


def martingale(start_sum: int, success_chance_percent_each_cycle: int, cycles: int) -> None:
    print("Stragety Name: Martingale")
    print(f"Start Sum: {start_sum}")
    print(f"Success Chance Percent Each Turn: {success_chance_percent_each_cycle}")
    print(f"Total Cycles: {cycles}\n")

    current_sum: int = start_sum
    win_cycle_count = 0
    lose_cycle_count = 0

    for cycle in range(cycles):
        print(f"Cycle: {cycle + 1}")
        if check_success(success_chance_percent_each_cycle):
            current_sum += 1

            win_cycle_count += 1
            print(f"  Win -> current sum: {current_sum}")
        else:
            current_sum -= 1

            lose_cycle_count += 1
            print(f"  Lose -> current sum: {current_sum}")

    print(f"\nEnd Sum: {current_sum} (win cycle count={win_cycle_count}) (lose cycle count={lose_cycle_count})")
