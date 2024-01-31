#!/usr/bin/python3
"""
Implementing MRUCache
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """ Initializes MRUCache"""
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the cache with MRU algorithm"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = max(self.cache_data, key=self.cache_data.get)
            print("DISCARD: {}".format(mru_key))
            del self.cache_data[mru_key]

        self.cache_data[key] = item

    def get(self, key):
        """ Gets an item from the cache by key"""
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value

        return value
