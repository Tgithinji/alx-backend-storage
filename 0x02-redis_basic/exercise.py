#!/usr/bin/env python3
""" exercise module """
from typing import Callable, Union
import redis
import uuid


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        instantiate the class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store the input data in Redis using the random key
        and return the key.
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        Retrieves data from the server
        """
        if not self._redis.exists(key):
            return None

        data = self._redis.get(key)

        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> Union[str, None]:
        """ Retrieving data with utf-8 conversion function """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """ Retrieving data with int conversion function """
        return self.get(key, lambda x: int(x))
