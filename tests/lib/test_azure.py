from typing import Union
from typing_extensions import Literal

import pytest

from wizkid._models import FinalRequestOptions
from wizkid.lib.azure import AzureWizkid, AsyncAzureWizkid

Client = Union[AzureWizkid, AsyncAzureWizkid]


sync_client = AzureWizkid(
    api_version="2023-07-01",
    api_key="example API key",
    azure_endpoint="https://example-resource.azure.wizkid.com",
)

async_client = AsyncAzureWizkid(
    api_version="2023-07-01",
    api_key="example API key",
    azure_endpoint="https://example-resource.azure.wizkid.com",
)


@pytest.mark.parametrize("client", [sync_client, async_client])
def test_implicit_deployment_path(client: Client) -> None:
    req = client._build_request(
        FinalRequestOptions.construct(
            method="post",
            url="/chat/completions",
            json_data={"model": "my-deployment-model"},
        )
    )
    assert (
        req.url
        == "https://example-resource.azure.wizkid.com/wizkid/deployments/my-deployment-model/chat/completions?api-version=2023-07-01"
    )


@pytest.mark.parametrize(
    "client,method",
    [
        (sync_client, "copy"),
        (sync_client, "with_options"),
        (async_client, "copy"),
        (async_client, "with_options"),
    ],
)
def test_client_copying(client: Client, method: Literal["copy", "with_options"]) -> None:
    if method == "copy":
        copied = client.copy()
    else:
        copied = client.with_options()

    assert copied._custom_query == {"api-version": "2023-07-01"}


@pytest.mark.parametrize(
    "client",
    [sync_client, async_client],
)
def test_client_copying_override_options(client: Client) -> None:
    copied = client.copy(
        api_version="2022-05-01",
    )
    assert copied._custom_query == {"api-version": "2022-05-01"}
