# strategy to use, (available: martingale, reverse_martingale, random_bet, fibonacci)
use_strategy: str = "fibonacci"
# runs this game nr of times (with detailed reports)
multi_game_cycles: int | None = None

# base configurations
base_config: dict[str, int | bool] = {
    "start_sum": 100,
    "success_chance_percent_each_cycle": 50,
    "cycles": 10,
    "log_verbose": False,
}

# strategy specific configuration
strategy_config: dict[str, dict[str, bool | int | list[int]]] = {
    "martingale": {
        "run_till_win": True
    },
    "reverse_martingale": {
        "target_sum_start_sum_percent": 5
    },
    "random_bet": {
        "bet_range": [1, 3]
    },
}
