# strategy to use, (available: martingale, reverse_martingale, random_bet)
use_strategy = "reverse_martingale"

# base configurations
base_config = {
    "start_sum": 100,
    "success_chance_percent_each_cycle": 50,
    "cycles": 10,
    "log_verbose": True,
}

# strategy specific configuration
strategy_config = {
    "martingale": {
        "run_till_win": True
    },
    "random_bet": {
        "bet_range": [1, 3]
    }
}
