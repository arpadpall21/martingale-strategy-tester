# strategy to use, (available: martingale, grand_martingale, anti_martingale, fibonacci, random_bet)
use_strategy: str = "martingale"
# runs this game nr of times (with detailed reports)
multi_game_cycles: int | None = None

# base configurations
base_config: dict[str, int | bool] = {
    "start_sum": 100,
    "success_chance_percent_each_cycle": 50,
    "cycles": 10,
    "log_verbose": True,
}

# strategy specific configuration
strategy_config: dict[str, dict[str, None | int | list[int]]] = {
    "martingale": {
        "percent_target": None
    },
    "grand_martingale": {
        "percent_target": None,
        "extra_bet": 1,
    },
    "anti_martingale": {
        "percent_target": None
    },
    "fibonacci": {
        "percent_target": None
    },
    "random_bet": {
        "bet_range": [1, 3]
    },
}
