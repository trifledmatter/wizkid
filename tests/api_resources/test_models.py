# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from wizkid import Wizkid, AsyncWizkid
from tests.utils import assert_matches_type
from wizkid.types import Model, ModelDeleted
from wizkid.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Wizkid) -> None:
        model = client.models.retrieve(
            "gpt-3.5-turbo",
        )
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Wizkid) -> None:
        response = client.models.with_raw_response.retrieve(
            "gpt-3.5-turbo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Wizkid) -> None:
        with client.models.with_streaming_response.retrieve(
            "gpt-3.5-turbo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(Model, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Wizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model` but received ''"):
            client.models.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Wizkid) -> None:
        model = client.models.list()
        assert_matches_type(SyncPage[Model], model, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Wizkid) -> None:
        response = client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(SyncPage[Model], model, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Wizkid) -> None:
        with client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(SyncPage[Model], model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Wizkid) -> None:
        model = client.models.delete(
            "ft:gpt-3.5-turbo:acemeco:suffix:abc123",
        )
        assert_matches_type(ModelDeleted, model, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Wizkid) -> None:
        response = client.models.with_raw_response.delete(
            "ft:gpt-3.5-turbo:acemeco:suffix:abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelDeleted, model, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Wizkid) -> None:
        with client.models.with_streaming_response.delete(
            "ft:gpt-3.5-turbo:acemeco:suffix:abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelDeleted, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Wizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model` but received ''"):
            client.models.with_raw_response.delete(
                "",
            )


class TestAsyncModels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWizkid) -> None:
        model = await async_client.models.retrieve(
            "gpt-3.5-turbo",
        )
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWizkid) -> None:
        response = await async_client.models.with_raw_response.retrieve(
            "gpt-3.5-turbo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWizkid) -> None:
        async with async_client.models.with_streaming_response.retrieve(
            "gpt-3.5-turbo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(Model, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model` but received ''"):
            await async_client.models.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncWizkid) -> None:
        model = await async_client.models.list()
        assert_matches_type(AsyncPage[Model], model, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWizkid) -> None:
        response = await async_client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(AsyncPage[Model], model, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWizkid) -> None:
        async with async_client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(AsyncPage[Model], model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncWizkid) -> None:
        model = await async_client.models.delete(
            "ft:gpt-3.5-turbo:acemeco:suffix:abc123",
        )
        assert_matches_type(ModelDeleted, model, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWizkid) -> None:
        response = await async_client.models.with_raw_response.delete(
            "ft:gpt-3.5-turbo:acemeco:suffix:abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelDeleted, model, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWizkid) -> None:
        async with async_client.models.with_streaming_response.delete(
            "ft:gpt-3.5-turbo:acemeco:suffix:abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelDeleted, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model` but received ''"):
            await async_client.models.with_raw_response.delete(
                "",
            )
