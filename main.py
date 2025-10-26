from dataclasses import fields
from typing import Any

from strategy import strategy, StragetyFn
from config import use_strategy, base_config, strategy_config, multi_game_cycles


def main():
    try:
        getattr(strategy, use_strategy)
    except AttributeError:
        print(
            f"Strategy not supported: {use_strategy} " +
            f"(suported strategies: {", ".join([field.name for field in fields(strategy)])})"
        )
        return

    strategy_fn: StragetyFn = getattr(strategy, use_strategy)
    config: dict[str, Any] = base_config
    if strategy_config.get(use_strategy):
        config["options"] = strategy_config[use_strategy]

    if multi_game_cycles and multi_game_cycles > 0:
        win_cycles: int = 0
        loss_cycles: int = 0
        balance: int = 0

        for game_id in range(multi_game_cycles):
            result: float = strategy_fn(**config)
            if result > 0:
                win_cycles += 1
                balance += result
            else:
                loss_cycles += 1
                balance -= result

        print(balance)

        # print(
        #     f"(win_cycles={win_cycles}) (loss_cycles={loss_cycles}) " +
        #     f"(start_sum={start_sum}) (sum_at_the_end_of_the_game={balance}) " +
        #     f"(net_balance={balance - start_sum}) (balance_ratio={round(balance / start_sum * 100, 1)}%)"
        # )
        
    else:
        strategy_fn(**config)


if __name__ == "__main__":
    main()
