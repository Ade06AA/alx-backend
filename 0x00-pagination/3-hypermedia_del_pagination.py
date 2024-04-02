#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def index_range(self, page: int, page_size: int):
        """
        doc
        """
        val: Tuple[int, int] = (page_size * page) - page_size, page_size * page
        return val

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        doc
        """
        assert isinstance(index, int)
        assert isinstance(page_size, int)
        assert index >= 0
        assert page_size > 0
        start, end = self.index_range(index + 1, page_size)
        fdata = self.dataset()
        data = fdata[start:end]
        hyper: Dict[str, Union[str, int, None, List]] = {}
        hyper["page_size"] = len(data)
        hyper["index"] = index
        hyper["data"] = data
        next_ = index + page_size
        hyper["next_index"] = next_ if next_ < len(fdata) else None
        return hyper
