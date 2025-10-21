from dataclasses import dataclass
from typing import Callable, Any

from strategy.martingale import martingale

type StragetyFn = Callable[[int, int, int, dict[str, Any]], None]


@dataclass
class Strategy():
    martingale: StragetyFn


strategy = Strategy(martingale=martingale)
