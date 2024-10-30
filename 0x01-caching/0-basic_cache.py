#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
"""
Created on wed Octo 25 15:06:00 2024

@Author: Elijah Tinayo
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    """
    def put(self, key, item):
        """
        Adds an item to the cache

        Args:
            key (str): key
            item (str): item
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache

        Args:
            key (str): key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
