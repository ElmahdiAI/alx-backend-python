#!/usr/bin/env python3
""" Let's duck type an iterable object """
from typing import List, Tuple
def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """ Element length """
    return [(i, len(i)) for i in lst]