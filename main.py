from dataclasses import fields
from typing import Any

from strategy import strategy, StragetyFn
from config import use_strategy, base_config, strategy_config


def main():
    try:
        getattr(strategy, use_strategy)
    except AttributeError:
        print(
            f"Strategy not supported: {use_strategy} " +
            f"(suported strategies: {", ".join([field.name for field in fields(strategy)])})"
        )
        return

    config: dict[str, Any] = base_config
    config["options"] = strategy_config[use_strategy]

    strategy_fn: StragetyFn = getattr(strategy, use_strategy)
    strategy_fn(**config,)


if __name__ == "__main__":
    main()
