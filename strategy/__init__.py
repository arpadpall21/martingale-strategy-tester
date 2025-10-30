from dataclasses import dataclass
from typing import Callable, Any, Optional

from strategy.martingale import martingale
from strategy.anti_martingale import anti_martingale
from strategy.grand_martingale import grand_martingale
from strategy.fibonacci import fibonacci
from strategy.pyramide_martingale import pyramide_martingale
from strategy.random_bet import random_bet

type StragetyFn = Callable[[int, int, int, bool, Optional[dict[str, Any]]], int]


@dataclass
class Strategy():
    martingale: StragetyFn
    grand_martingale: StragetyFn
    random_bet: StragetyFn
    fibonacci: StragetyFn
    pyramide_martingale: StragetyFn
    anti_martingale: StragetyFn


strategy = Strategy(
    martingale=martingale,
    grand_martingale=grand_martingale,
    anti_martingale=anti_martingale,
    fibonacci=fibonacci,
    pyramide_martingale=pyramide_martingale,
    random_bet=random_bet,
)
