#!/usr/bin/python3
""" Python caching systems """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRU caching system
    Use of OrderedDict which keep order of insertion of keys
    The order shows how recently they were used.
    """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        First, add/ update the key by conventional methods.
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(discarded[0]))

    def get(self, key):
        """ Get an item by key
        Return the value of the key that is queried in O(1)
        and return -1 if the key is not found.
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
