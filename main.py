from strategy import strategy

start_sum = 10_000
success_chance_percent_each_cycle = 47.4
cycles: int = 100
log_verbose: bool = True


def main():
    # call strategy here...
    strategy.martingale(start_sum, success_chance_percent_each_cycle, cycles, log_verbose)


if __name__ == "__main__":
    main()
