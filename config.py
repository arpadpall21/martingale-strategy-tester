# strategy to use, (available: martingale)
use_strategy = "martingale"

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
    }
}
