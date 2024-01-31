#!/usr/bin/env python3
"""
Implementation of a basic caching system
using BasicCache that inherits from BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """_BasicCache class that inherits from BaseCaching"""

    def __init__(self):
        """initializing the class"""
        super().__init__()

    def put(self, key, item):
        """adds items in the cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """retrieves values from the cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
