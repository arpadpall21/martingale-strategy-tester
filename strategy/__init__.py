from dataclasses import dataclass
from typing import Callable, Any, Optional

from strategy.martingale import martingale
from strategy.random_bet import random_bet

type StragetyFn = Callable[[int, int, int, bool, Optional[dict[str, Any]]], int]


@dataclass
class Strategy():
    martingale: StragetyFn
    random_bet: StragetyFn


strategy = Strategy(martingale=martingale, random_bet=random_bet)
