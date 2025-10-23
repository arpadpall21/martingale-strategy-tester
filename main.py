from strategy import strategy

start_sum = 10
success_chance_percent_each_cycle = 47.4
cycles: int = 10
break_on_empty_balance: bool = True


def main():
    # call strategy here...
    strategy.martingale(start_sum, success_chance_percent_each_cycle, cycles, break_on_empty_balance)


if __name__ == "__main__":
    main()
