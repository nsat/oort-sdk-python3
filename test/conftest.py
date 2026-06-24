# coding: utf-8

"""Shared pytest fixtures for generated API client tests."""

import pytest

from oort_sdk_client.api_client import ApiClient
from oort_sdk_client.configuration import Configuration


@pytest.fixture
def configuration():
    """Default client configuration (set host, verify_ssl, access_token, etc. in tests)."""
    return Configuration()


@pytest.fixture
def api_client(configuration):
    """HTTP layer used by all API facade classes."""
    return ApiClient(configuration)


@pytest.fixture
def sdk_api_client(api_client):
    """SdkApi using the shared ``api_client`` fixture."""
    from oort_sdk_client.api.sdk_api import SdkApi
    return SdkApi(api_client=api_client)


