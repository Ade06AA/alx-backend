#!/usr/bin/env python3
from typing import Tuple
"""
doc
"""


def index_range(page: int, page_size: int):
    """
    doc
    """
    val: Tuple[int, int] = (page_size * page) - page_size, page_size * page
    return val
