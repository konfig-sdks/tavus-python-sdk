# coding: utf-8
"""
    Tavus Developer API Collection

    We're an AI video research company making personalized video possible at scale. Generate videos of yourself, and never record again! Available via web app & developer APIs.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import typing

from tavus_python_sdk.configuration import Configuration
from tavus_python_sdk.api_client import ApiClient



class ClientCustom:

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        # customize here

    # add custom methods here