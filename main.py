from strategy import strategy, StragetyFn
from config import use_strategy, config


def main():
    strategy_fn: StragetyFn = getattr(strategy, use_strategy)
    strategy_fn(**config,)


if __name__ == "__main__":
    main()
