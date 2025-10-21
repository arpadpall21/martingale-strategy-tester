from strategy import strategy

start_sum = 1_000
success_chance_percent_each_cycle = 50
cycles: int = 10


def main():
    # call strategy here...
    strategy.martingale(start_sum, success_chance_percent_each_cycle, cycles)


if __name__ == "__main__":
    main()
