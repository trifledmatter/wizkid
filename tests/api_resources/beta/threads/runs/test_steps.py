# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from wizkid import Wizkid, AsyncWizkid
from tests.utils import assert_matches_type
from wizkid.pagination import SyncCursorPage, AsyncCursorPage
from wizkid.types.beta.threads.runs import RunStep

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSteps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Wizkid) -> None:
        step = client.beta.threads.runs.steps.retrieve(
            "string",
            thread_id="string",
            run_id="string",
        )
        assert_matches_type(RunStep, step, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Wizkid) -> None:
        response = client.beta.threads.runs.steps.with_raw_response.retrieve(
            "string",
            thread_id="string",
            run_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(RunStep, step, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Wizkid) -> None:
        with client.beta.threads.runs.steps.with_streaming_response.retrieve(
            "string",
            thread_id="string",
            run_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(RunStep, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Wizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.steps.with_raw_response.retrieve(
                "string",
                thread_id="",
                run_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.steps.with_raw_response.retrieve(
                "string",
                thread_id="string",
                run_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.beta.threads.runs.steps.with_raw_response.retrieve(
                "",
                thread_id="string",
                run_id="string",
            )

    @parametrize
    def test_method_list(self, client: Wizkid) -> None:
        step = client.beta.threads.runs.steps.list(
            "string",
            thread_id="string",
        )
        assert_matches_type(SyncCursorPage[RunStep], step, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Wizkid) -> None:
        step = client.beta.threads.runs.steps.list(
            "string",
            thread_id="string",
            after="string",
            before="string",
            limit=0,
            order="asc",
        )
        assert_matches_type(SyncCursorPage[RunStep], step, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Wizkid) -> None:
        response = client.beta.threads.runs.steps.with_raw_response.list(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(SyncCursorPage[RunStep], step, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Wizkid) -> None:
        with client.beta.threads.runs.steps.with_streaming_response.list(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(SyncCursorPage[RunStep], step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Wizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.steps.with_raw_response.list(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.steps.with_raw_response.list(
                "",
                thread_id="string",
            )


class TestAsyncSteps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWizkid) -> None:
        step = await async_client.beta.threads.runs.steps.retrieve(
            "string",
            thread_id="string",
            run_id="string",
        )
        assert_matches_type(RunStep, step, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWizkid) -> None:
        response = await async_client.beta.threads.runs.steps.with_raw_response.retrieve(
            "string",
            thread_id="string",
            run_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(RunStep, step, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWizkid) -> None:
        async with async_client.beta.threads.runs.steps.with_streaming_response.retrieve(
            "string",
            thread_id="string",
            run_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(RunStep, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.steps.with_raw_response.retrieve(
                "string",
                thread_id="",
                run_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.steps.with_raw_response.retrieve(
                "string",
                thread_id="string",
                run_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.beta.threads.runs.steps.with_raw_response.retrieve(
                "",
                thread_id="string",
                run_id="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncWizkid) -> None:
        step = await async_client.beta.threads.runs.steps.list(
            "string",
            thread_id="string",
        )
        assert_matches_type(AsyncCursorPage[RunStep], step, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWizkid) -> None:
        step = await async_client.beta.threads.runs.steps.list(
            "string",
            thread_id="string",
            after="string",
            before="string",
            limit=0,
            order="asc",
        )
        assert_matches_type(AsyncCursorPage[RunStep], step, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWizkid) -> None:
        response = await async_client.beta.threads.runs.steps.with_raw_response.list(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(AsyncCursorPage[RunStep], step, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWizkid) -> None:
        async with async_client.beta.threads.runs.steps.with_streaming_response.list(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(AsyncCursorPage[RunStep], step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncWizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.steps.with_raw_response.list(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.steps.with_raw_response.list(
                "",
                thread_id="string",
            )
