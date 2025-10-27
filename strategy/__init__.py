from dataclasses import dataclass
from typing import Callable, Any, Optional

from strategy.martingale import martingale
from strategy.reverse_martingale import reverse_martingale
from strategy.random_bet import random_bet
from strategy.fibonacci import fibonacci

type StragetyFn = Callable[[int, int, int, bool, Optional[dict[str, Any]]], int]


@dataclass
class Strategy():
    martingale: StragetyFn
    random_bet: StragetyFn
    reverse_martingale: StragetyFn
    fibonacci: StragetyFn


strategy = Strategy(
    martingale=martingale,
    reverse_martingale=reverse_martingale,
    random_bet=random_bet,
    fibonacci=fibonacci,
)
