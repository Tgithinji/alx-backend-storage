#!/usr/bin/env python3
""" exercise module """
from typing import Union
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
