"""
    Available Strategies:
        - martingale
        - grand_martingale
        - anti_martingale
        - fibonacci
        - pyramid_martingale
        - random_bet
"""
use_strategy: str = "pyramid_martingale"
multi_game_cycles: int | None = None

# base configurations
base_config: dict[str, int | bool] = {
    "start_sum": 100,
    "success_chance_percent_each_cycle": 50,
    "cycles": 100,
    "log_verbose": True,
    "percent_target": None,
}

# strategy specific configuration
strategy_config: dict[str, dict[str, int | float | list[int]]] = {
    "grand_martingale": {
        "extra_bet": 1,
    },
    "pyramid_martingale": {
        "multiplier": 1.5,
    },
    "random_bet": {
        "bet_range": [1, 3]
    },
}
