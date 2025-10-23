use_strategy = "martingale"

strategy_config = {
    "martingale": {
        "run_till_win": True
    }
}

config = {
    "start_sum": 100,
    "success_chance_percent_each_cycle": 50,
    "cycles": 10,
    "log_verbose": True,
    "options": strategy_config[use_strategy]
}
