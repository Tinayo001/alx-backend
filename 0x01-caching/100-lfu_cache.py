#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed octo  30 16:50:00 2024

@Author: Tinayo Keiya
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.queue = []
        self.counter = {}

    def put(self, key, item):
        """
        Adds an item to the cache

        Args:
        key (str) - key
        item (str) - item
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        item_count = self.counter.get(key, None)

        if item_count is not None:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                del self.counter[first]
                print("DISCARD: {}".format(first))

        if key not in self.queue:
            self.queue.insert(0, key)
        self.move_right_list(key)

    def get(self, key):
        """
        Retrieve an item from the cache

        Args:
            key (str) - key
        """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.counter[key] += 1
            self.move_right_list(key)
        return item

    def move_right_list(self, item):
        """
        Moves element to the right, taking into account LFU

        Args:
            item (str) - item

        Returns:
            None
        """
        length = len(self.queue)

        idx = self.queue.index(item)
        item_count = self.counter[item]

        for i in range(idx, length):
            if i != (length - 1):
                nxt = self.queue[i + 1]
                nxt_count = self.counter[nxt]

                if nxt_count > item_count:
                    break

        self.queue.insert(i + 1, item)
        self.queue.remove(item)

    @staticmethod
    def get_first_list(array):
        """
        Get first element of list or None

        Args:
            array (list) - list

        Returns:
            array[0] - first element
        """
        return array[0] if array else None
