# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Coward
@Version        :  
------------------------------------
@File           :  utils.py
@Description    :  
@CreateTime     :  2023/9/28 19:14
------------------------------------
@ModifyTime     :  
"""
from __future__ import annotations

from re import findall
import os
import json
from typing import Any, Type, Union


def _choose_path(filename: str) -> str:
    """
    Choose the path for the filename.

    :param filename: The input filename.
    :type filename: str

    :returns: str: The chosen filename or path.
    """
    if findall(r'/', filename) == '/':
        return filename
    else:
        filename = os.getcwd() + '/' + filename
        return filename

def write_Proxy_List(filename: str, proxy_list: Union[list, dict]) -> bool | Any:
    """
    Write a proxy list to a file.

    :param filename: The name of the file to write the proxy list to.
    :type filename: str

    :param proxy_list: The proxy list to write to the file.
    :type proxy_list: Union[list, dict]

    :returns: bool: True if the write operation is successful.
    :raises IOError: If there is an error while writing to the file.
    """
    filename = _choose_path(filename)

    try:
        with open(filename, 'w') as f:
            json.dump(proxy_list, f)
        return True

    except IOError as error:
        return error

def read_Proxy_List(filename: str) -> Union[dict, IOError]:
    """
    Read a proxy list from a file.

    :param filename: The name of the file to read the proxy list from.
    :type filename: str

    :returns: Union[dict, IOError]: A dictionary containing the proxy list if the read operation is successful.
        IOError if there is an error while reading from the file.
    """
    filename = _choose_path(filename)

    try:
        with open(filename, 'r') as json_file:
            data_dict = json.load(json_file)
            return data_dict

    except IOError as error:
        return error

def delete_Proxy_List(filename: str) -> Union[None, Type[FileNotFoundError], Exception]:
    """
    Delete a proxy list file.

    :param filename: The name of the file to delete.
    :type filename: str

    :returns: None: If the file is deleted successfully.
    :raises FileNotFoundError: If the file to be deleted is not found.
    :raises Exception: If there is an error while deleting the file.
    """
    filename = _choose_path(filename)

    try:
        os.remove(filename)
        return None
    except FileNotFoundError:
        return FileNotFoundError
    except Exception as e:
        return e
