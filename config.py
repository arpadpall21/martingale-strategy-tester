# strategy to use, (available: martingale, grand_martingale, anti_martingale, fibonacci, random_bet)
use_strategy: str = "anti_martingale"
# runs this game nr of times (with detailed reports)
multi_game_cycles: int | None = None

# base configurations
base_config: dict[str, int | bool] = {
    "start_sum": 100,
    "success_chance_percent_each_cycle": 50,
    "cycles": 10,
    "log_verbose": True,
    "percent_target": 1,
}

# strategy specific configuration
strategy_config: dict[str, dict[str, None | int | list[int]]] = {
    "grand_martingale": {
        "extra_bet": 1,
    },
    "random_bet": {
        "bet_range": [1, 3]
    },
}
