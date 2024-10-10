#!/usr/bin/env python3
""" More involved type annotations  """
from typing import TypeVar, Mapping, Optional

T = TypeVar('T')

def safely_get_value(dct: Mapping, key, default: Optional[T] = None) -> Optional[T]:
    """ Safely get value """
    if key in dct:
        return dct[key]
    else:
        return default

