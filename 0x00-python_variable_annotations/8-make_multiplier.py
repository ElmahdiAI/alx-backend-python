#!/usr/bin/env python3
"""  Complex types - functions """
from typing import Callable
def make_multiplier (multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument,
    returns a function that multiplies a float by multiplier.
    """
    def fct (value: float) ->float:
        return value * multiplier
    return fct
