"""
    Random Strategy:
      - betting randomly while randomly changing the bet size
"""
from typing import Any


def random(start_sum: int,
           success_chance_percent_each_cycle: int,
           cycles: int,
           log_verbose: bool,
           options: dict[str, Any] = {"bet_size": [1, 1]}) -> int:

    return 0
