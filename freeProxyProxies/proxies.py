# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Coward
@Version        :
------------------------------------
@File           :  proxies.py
@Description    :
@CreateTime     :  2023/9/26 11:44
------------------------------------
@ModifyTime     :
"""

from requests import *
from re import findall
from .models import ReceiveProxy

regex = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+\b'

class Proxies(ReceiveProxy):
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
        super().__init__()

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

    def ssl_Proxy(self) -> list:
        """
        Fetch a list of SSL proxies from 'https://www.sslproxies.org/'.

        :returns: list: A list of SSL proxy addresses in the format 'IP:Port'.
        """
        url = 'https://www.sslproxies.org/'
        response = get(url=url, headers=self.HEADERS).text
        ssl_Proxy_List = findall(regex, response)
        return ssl_Proxy_List

    def free_Proxy(self) -> list:
        """
        Fetch a list of free proxies from 'https://free-proxy-list.net/'.

        :returns: list: A list of free proxy addresses in the format 'IP:Port'.
        """
        url = 'https://free-proxy-list.net/'
        response = get(url=url, headers=self.HEADERS).text
        free_Proxy_List = findall(regex, response)
        return free_Proxy_List

    def US_Proxy(self) -> list:
        """
        Fetch a list of US proxies from 'https://www.us-proxy.org/'.

        :returns: list: A list of US proxy addresses in the format 'IP:Port'.
        """
        url = 'https://www.us-proxy.org/'
        response = get(url=url, headers=self.HEADERS).text
        us_Proxy_List = findall(regex, response)
        return us_Proxy_List

    def UK_Proxy(self) -> list:
        """
        Fetch a list of UK proxies from 'https://free-proxy-list.net/uk-proxy.html.

        :returns: list: A list of UK proxy addresses in the format 'IP:Port'.
        """
        url = 'https://free-proxy-list.net/uk-proxy.html'
        response = get(url=url, headers=self.HEADERS).text
        uk_Proxy_List = findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+\b', response)
        return uk_Proxy_List

    def anonymous_Proxy(self) -> list:
        """
        Fetch a list of anonymous proxies from 'https://free-proxy-list.net/anonymous-proxy.html'.

        :returns: list: A list of anonymous proxy addresses in the format 'IP:Port'.
        """
        url = 'https://free-proxy-list.net/anonymous-proxy.html'
        response = get(url=url, headers=self.HEADERS).text
        anonymous_Proxy_List = findall(regex, response)
        return anonymous_Proxy_List

    def all_Proxy(self) -> dict:
        """
        Fetch all available proxy lists.

        :returns: dict: A dictionary containing proxy lists for various categories.
        """
        all_Proxy = {
            'sslProxy':  Proxies.free_Proxy(self),
            'free_Proxy': Proxies.free_Proxy(self),
            'us_Proxy': Proxies.US_Proxy(self),
            'uk_Proxy': Proxies.UK_Proxy(self),
            'anonymous_Proxy': Proxies.anonymous_Proxy(self),
        }
        return all_Proxy
