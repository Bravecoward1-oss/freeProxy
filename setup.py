# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Coward
@Version        :  
------------------------------------
@File           :  setup.py
@Description    :  
@CreateTime     :  2023/10/7 00:38
------------------------------------
@ModifyTime     :  
"""

import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


VERSION = '0.1.2'

setup(
    name='freeProxyProxies',  # package name
    version=VERSION,  # package version
    description='freeProxyProxies',  # package description
    author='Coward',
    author_email='CryingCoward@proton.me',
    install_requires=['requests'],
    long_description=README,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'freeProxyProxies = src.freeProxyProxies:main',
        ],
    }
)

