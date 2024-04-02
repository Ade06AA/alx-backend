#!/usr/bin/env python3
"""
doc
"""
import csv
import math
from typing import List, Tuple, Dict, Union
from math import ceil




class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        doc
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def index_range(self, page: int, page_size: int):
        """
        doc
        """
        val: Tuple[int, int] = (page_size * page) - page_size, page_size * page
        return val

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[List, str, None, int]]:
        """
        doc
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start, end = self.index_range(page, page_size)
        fdata = self.dataset()
        data = fdata[start:end]
        hyper: Dict[str, Union[str, int, None, List]]= {}
        hyper["page_size"] = len(data)
        hyper["page"] = page
        hyper["data"] = data
        total = len(fdata) / page_size
        total = ceil(total)
        hyper["next_page"] = page + 1 if page != total else None
        hyper["prev_page"] = None if page < 2 else page - 1
        hyper["total_page"] = total
        return hyper
