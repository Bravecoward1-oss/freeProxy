# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Coward
@Version        :  
------------------------------------
@File           :  api.py
@Description    :  
@CreateTime     :  2023/9/29 00:47
------------------------------------
@ModifyTime     :  
"""

from .proxies import Proxies

proxies = Proxies()

def ssl_Proxy() -> list:
    """
    Fetch a list of SSL proxies.

    :returns: list: A list of SSL proxy addresses in the format 'IP:Port'.
    """
    return proxies.ssl_Proxy()

def free_Proxy() -> list:
    """
    Fetch a list of free proxies.

    :returns: list: A list of free proxy addresses in the format 'IP:Port'.
    """
    return proxies.free_Proxy()

def UK_Proxy() -> list:
    """
    Fetch a list of UK proxies.

    :returns: list: A list of UK proxy addresses in the format 'IP:Port'.
    """
    return proxies.UK_Proxy()

def US_Proxy() -> list:
    """
    Fetch a list of US proxies.

    :returns: list: A list of US proxy addresses in the format 'IP:Port'.
    """
    return proxies.US_Proxy()

def anonymous_Proxy() -> list:
    """
    Fetch a list of anonymous proxies.

    :returns: list: A list of anonymous proxy addresses in the format 'IP:Port'.
    """
    return proxies.anonymous_Proxy()

def all_Proxy() -> dict:
    """
    Fetch all available proxy lists.

    :returns: dict: A dictionary containing proxy lists for various categories.
        - 'sslProxy': A list of SSL proxy addresses in the format 'IP:Port'.
        - 'free_Proxy': A list of free proxy addresses in the format 'IP:Port'.
        - 'us_Proxy': A list of US proxy addresses in the format 'IP:Port'.
        - 'uk_Proxy': A list of UK proxy addresses in the format 'IP:Port'.
        - 'anonymous_Proxy': A list of anonymous proxy addresses in the format 'IP:Port'.
    """
    return proxies.all_Proxy()
