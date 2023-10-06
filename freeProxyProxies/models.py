# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Coward
@Version        :
------------------------------------
@File           :  models.py
@Description    :
@CreateTime     :  2023/9/28 19:14
------------------------------------
@ModifyTime     :
"""

from abc import ABC, abstractmethod

class ReceiveProxy(ABC):
    """
    Receive_Proxy is a class for fetching proxy lists from various sources.

    Attributes:
        HEADERS (dict): Default HTTP headers for making requests.
    """

    def __init__(self):
        """
        Initialize the Receive_Proxy class.

        This constructor sets up the default HTTP headers.
        """
        self.HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/87.0.4280.88 Mobile Safardadi/537.36 '
        }

    def __getattr__(self, name):
        """
        Custom attribute access method.

        :param name: The name of the attribute being accessed.
        :type name: str

        :returns: Callable: If the attribute exists and is callable, return it.
        :raises AttributeError: If the attribute does not exist.
        """
        if name in dir(self) and callable(getattr(self, name)):
            return getattr(self, name)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    @abstractmethod
    def ssl_Proxy(self) -> list:
        """
        Fetch a list of SSL proxies.

        :returns: list: A list of SSL proxy addresses in the format 'IP:Port'.
        """
        pass

    @abstractmethod
    def free_Proxy(self) -> list:
        """
        Fetch a list of free proxies.

        :returns: list: A list of free proxy addresses in the format 'IP:Port'.
        """
        pass

    @abstractmethod
    def all_Proxy(self) -> dict:
        """
        Fetch all available proxy lists.

        :returns: dict: A dictionary containing proxy lists for various categories.
        """
        pass
