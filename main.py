from dataclasses import fields
from typing import Any

from strategy import strategy, StragetyFn
from config import use_strategy, base_config, strategy_config, multi_game_cycles
from misc.log import log_multi_game


def main():
    try:
        getattr(strategy, use_strategy)
    except AttributeError:
        raise ValueError(
            f"Strategy not supported: {use_strategy} " +
            f"(suported strategies: {", ".join([field.name for field in fields(strategy)])})"
        )

    strategy_fn: StragetyFn = getattr(strategy, use_strategy)
    config: dict[str, Any] = base_config
    if strategy_config.get(use_strategy):
        config["options"] = strategy_config[use_strategy]

    if multi_game_cycles and multi_game_cycles > 0:
        win_cycles: int = 0
        loss_cycles: int = 0
        balance: int | float = 0

        for game_id in range(multi_game_cycles):
            result: float = strategy_fn(**config)
            if result > 0:
                win_cycles += 1
                balance += result
            else:
                loss_cycles += 1
                balance -= result
        log_multi_game(base_config, multi_game_cycles, win_cycles, loss_cycles, balance)
    else:
        strategy_fn(**config)


if __name__ == "__main__":
    main()
