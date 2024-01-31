#!/usr/bin/python3
"""
Implementation of FIFO Cache
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCAching"""

    def __init__(self):
        """ Initialize FIFOCache"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get the first item inserted (oldest)
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from the cache"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
