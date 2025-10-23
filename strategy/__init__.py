from dataclasses import dataclass
from typing import Callable, Any

from strategy.martingale import martingale

type StragetyFn = Callable[[int, int, int, bool, dict[str, Any]], int]


@dataclass
class Strategy():
    martingale: StragetyFn


strategy = Strategy(martingale=martingale)
