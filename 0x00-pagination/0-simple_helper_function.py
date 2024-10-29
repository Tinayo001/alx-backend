#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday Octo 22 2024 09:45:00

@Author: Tinayo Keiya
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns start and end index for pagination

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple: start and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
