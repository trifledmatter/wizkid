# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os as _os

import httpx
import pytest
from httpx import URL

import wizkid
from wizkid import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES


def reset_state() -> None:
    wizkid._reset_client()
    wizkid.api_key = None or "My API Key"
    wizkid.organization = None
    wizkid.base_url = None
    wizkid.timeout = DEFAULT_TIMEOUT
    wizkid.max_retries = DEFAULT_MAX_RETRIES
    wizkid.default_headers = None
    wizkid.default_query = None
    wizkid.http_client = None
    wizkid.api_type = _os.environ.get("WIZKID_API_TYPE")  # type: ignore
    wizkid.api_version = None
    wizkid.azure_endpoint = None
    wizkid.azure_ad_token = None
    wizkid.azure_ad_token_provider = None


@pytest.fixture(autouse=True)
def reset_state_fixture() -> None:
    reset_state()


def test_base_url_option() -> None:
    assert wizkid.base_url is None
    assert wizkid.completions._client.base_url == URL("https://api.wizkid.com/v1/")

    wizkid.base_url = "http://foo.com"

    assert wizkid.base_url == URL("http://foo.com")
    assert wizkid.completions._client.base_url == URL("http://foo.com")


def test_timeout_option() -> None:
    assert wizkid.timeout == wizkid.DEFAULT_TIMEOUT
    assert wizkid.completions._client.timeout == wizkid.DEFAULT_TIMEOUT

    wizkid.timeout = 3

    assert wizkid.timeout == 3
    assert wizkid.completions._client.timeout == 3


def test_max_retries_option() -> None:
    assert wizkid.max_retries == wizkid.DEFAULT_MAX_RETRIES
    assert wizkid.completions._client.max_retries == wizkid.DEFAULT_MAX_RETRIES

    wizkid.max_retries = 1

    assert wizkid.max_retries == 1
    assert wizkid.completions._client.max_retries == 1


def test_default_headers_option() -> None:
    assert wizkid.default_headers == None

    wizkid.default_headers = {"Foo": "Bar"}

    assert wizkid.default_headers["Foo"] == "Bar"
    assert wizkid.completions._client.default_headers["Foo"] == "Bar"


def test_default_query_option() -> None:
    assert wizkid.default_query is None
    assert wizkid.completions._client._custom_query == {}

    wizkid.default_query = {"Foo": {"nested": 1}}

    assert wizkid.default_query["Foo"] == {"nested": 1}
    assert wizkid.completions._client._custom_query["Foo"] == {"nested": 1}


def test_http_client_option() -> None:
    assert wizkid.http_client is None

    original_http_client = wizkid.completions._client._client
    assert original_http_client is not None

    new_client = httpx.Client()
    wizkid.http_client = new_client

    assert wizkid.completions._client._client is new_client


import contextlib
from typing import Iterator

from wizkid.lib.azure import AzureWizkid


@contextlib.contextmanager
def fresh_env() -> Iterator[None]:
    old = _os.environ.copy()

    try:
        _os.environ.clear()
        yield
    finally:
        _os.environ.update(old)


def test_only_api_key_results_in_wizkid_api() -> None:
    with fresh_env():
        wizkid.api_type = None
        wizkid.api_key = "example API key"

        assert type(wizkid.completions._client).__name__ == "_ModuleClient"


def test_azure_api_key_env_without_api_version() -> None:
    with fresh_env():
        wizkid.api_type = None
        _os.environ["AZURE_WIZKID_API_KEY"] = "example API key"

        with pytest.raises(
            ValueError,
            match=r"Must provide either the `api_version` argument or the `WIZKID_API_VERSION` environment variable",
        ):
            wizkid.completions._client  # noqa: B018


def test_azure_api_key_and_version_env() -> None:
    with fresh_env():
        wizkid.api_type = None
        _os.environ["AZURE_WIZKID_API_KEY"] = "example API key"
        _os.environ["WIZKID_API_VERSION"] = "example-version"

        with pytest.raises(
            ValueError,
            match=r"Must provide one of the `base_url` or `azure_endpoint` arguments, or the `AZURE_WIZKID_ENDPOINT` environment variable",
        ):
            wizkid.completions._client  # noqa: B018


def test_azure_api_key_version_and_endpoint_env() -> None:
    with fresh_env():
        wizkid.api_type = None
        _os.environ["AZURE_WIZKID_API_KEY"] = "example API key"
        _os.environ["WIZKID_API_VERSION"] = "example-version"
        _os.environ["AZURE_WIZKID_ENDPOINT"] = "https://www.example"

        wizkid.completions._client  # noqa: B018

        assert wizkid.api_type == "azure"


def test_azure_azure_ad_token_version_and_endpoint_env() -> None:
    with fresh_env():
        wizkid.api_type = None
        _os.environ["AZURE_WIZKID_AD_TOKEN"] = "example AD token"
        _os.environ["WIZKID_API_VERSION"] = "example-version"
        _os.environ["AZURE_WIZKID_ENDPOINT"] = "https://www.example"

        client = wizkid.completions._client
        assert isinstance(client, AzureWizkid)
        assert client._azure_ad_token == "example AD token"


def test_azure_azure_ad_token_provider_version_and_endpoint_env() -> None:
    with fresh_env():
        wizkid.api_type = None
        _os.environ["WIZKID_API_VERSION"] = "example-version"
        _os.environ["AZURE_WIZKID_ENDPOINT"] = "https://www.example"
        wizkid.azure_ad_token_provider = lambda: "token"

        client = wizkid.completions._client
        assert isinstance(client, AzureWizkid)
        assert client._azure_ad_token_provider is not None
        assert client._azure_ad_token_provider() == "token"
