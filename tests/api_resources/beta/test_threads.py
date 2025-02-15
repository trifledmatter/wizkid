# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from wizkid import Wizkid, AsyncWizkid
from tests.utils import assert_matches_type
from wizkid.types.beta import (
    Thread,
    ThreadDeleted,
)
from wizkid.types.beta.threads import Run

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Wizkid) -> None:
        thread = client.beta.threads.create()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Wizkid) -> None:
        thread = client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": "x",
                    "file_ids": ["string"],
                    "metadata": {},
                },
                {
                    "role": "user",
                    "content": "x",
                    "file_ids": ["string"],
                    "metadata": {},
                },
                {
                    "role": "user",
                    "content": "x",
                    "file_ids": ["string"],
                    "metadata": {},
                },
            ],
            metadata={},
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Wizkid) -> None:
        response = client.beta.threads.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Wizkid) -> None:
        with client.beta.threads.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(Thread, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Wizkid) -> None:
        thread = client.beta.threads.retrieve(
            "string",
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Wizkid) -> None:
        response = client.beta.threads.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Wizkid) -> None:
        with client.beta.threads.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(Thread, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Wizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Wizkid) -> None:
        thread = client.beta.threads.update(
            "string",
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Wizkid) -> None:
        thread = client.beta.threads.update(
            "string",
            metadata={},
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Wizkid) -> None:
        response = client.beta.threads.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Wizkid) -> None:
        with client.beta.threads.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(Thread, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Wizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Wizkid) -> None:
        thread = client.beta.threads.delete(
            "string",
        )
        assert_matches_type(ThreadDeleted, thread, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Wizkid) -> None:
        response = client.beta.threads.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadDeleted, thread, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Wizkid) -> None:
        with client.beta.threads.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadDeleted, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Wizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_create_and_run_overload_1(self, client: Wizkid) -> None:
        thread = client.beta.threads.create_and_run(
            assistant_id="string",
        )
        assert_matches_type(Run, thread, path=["response"])

    @parametrize
    def test_method_create_and_run_with_all_params_overload_1(self, client: Wizkid) -> None:
        thread = client.beta.threads.create_and_run(
            assistant_id="string",
            instructions="string",
            metadata={},
            model="string",
            stream=False,
            thread={
                "messages": [
                    {
                        "role": "user",
                        "content": "x",
                        "file_ids": ["string"],
                        "metadata": {},
                    },
                    {
                        "role": "user",
                        "content": "x",
                        "file_ids": ["string"],
                        "metadata": {},
                    },
                    {
                        "role": "user",
                        "content": "x",
                        "file_ids": ["string"],
                        "metadata": {},
                    },
                ],
                "metadata": {},
            },
            tools=[{"type": "code_interpreter"}, {"type": "code_interpreter"}, {"type": "code_interpreter"}],
        )
        assert_matches_type(Run, thread, path=["response"])

    @parametrize
    def test_raw_response_create_and_run_overload_1(self, client: Wizkid) -> None:
        response = client.beta.threads.with_raw_response.create_and_run(
            assistant_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Run, thread, path=["response"])

    @parametrize
    def test_streaming_response_create_and_run_overload_1(self, client: Wizkid) -> None:
        with client.beta.threads.with_streaming_response.create_and_run(
            assistant_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(Run, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_and_run_overload_2(self, client: Wizkid) -> None:
        thread_stream = client.beta.threads.create_and_run(
            assistant_id="string",
            stream=True,
        )
        thread_stream.response.close()

    @parametrize
    def test_method_create_and_run_with_all_params_overload_2(self, client: Wizkid) -> None:
        thread_stream = client.beta.threads.create_and_run(
            assistant_id="string",
            stream=True,
            instructions="string",
            metadata={},
            model="string",
            thread={
                "messages": [
                    {
                        "role": "user",
                        "content": "x",
                        "file_ids": ["string"],
                        "metadata": {},
                    },
                    {
                        "role": "user",
                        "content": "x",
                        "file_ids": ["string"],
                        "metadata": {},
                    },
                    {
                        "role": "user",
                        "content": "x",
                        "file_ids": ["string"],
                        "metadata": {},
                    },
                ],
                "metadata": {},
            },
            tools=[{"type": "code_interpreter"}, {"type": "code_interpreter"}, {"type": "code_interpreter"}],
        )
        thread_stream.response.close()

    @parametrize
    def test_raw_response_create_and_run_overload_2(self, client: Wizkid) -> None:
        response = client.beta.threads.with_raw_response.create_and_run(
            assistant_id="string",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_and_run_overload_2(self, client: Wizkid) -> None:
        with client.beta.threads.with_streaming_response.create_and_run(
            assistant_id="string",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncThreads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncWizkid) -> None:
        thread = await async_client.beta.threads.create()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWizkid) -> None:
        thread = await async_client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": "x",
                    "file_ids": ["string"],
                    "metadata": {},
                },
                {
                    "role": "user",
                    "content": "x",
                    "file_ids": ["string"],
                    "metadata": {},
                },
                {
                    "role": "user",
                    "content": "x",
                    "file_ids": ["string"],
                    "metadata": {},
                },
            ],
            metadata={},
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWizkid) -> None:
        response = await async_client.beta.threads.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWizkid) -> None:
        async with async_client.beta.threads.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(Thread, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWizkid) -> None:
        thread = await async_client.beta.threads.retrieve(
            "string",
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWizkid) -> None:
        response = await async_client.beta.threads.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWizkid) -> None:
        async with async_client.beta.threads.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(Thread, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncWizkid) -> None:
        thread = await async_client.beta.threads.update(
            "string",
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWizkid) -> None:
        thread = await async_client.beta.threads.update(
            "string",
            metadata={},
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWizkid) -> None:
        response = await async_client.beta.threads.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWizkid) -> None:
        async with async_client.beta.threads.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(Thread, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncWizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncWizkid) -> None:
        thread = await async_client.beta.threads.delete(
            "string",
        )
        assert_matches_type(ThreadDeleted, thread, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWizkid) -> None:
        response = await async_client.beta.threads.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadDeleted, thread, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWizkid) -> None:
        async with async_client.beta.threads.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadDeleted, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWizkid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_create_and_run_overload_1(self, async_client: AsyncWizkid) -> None:
        thread = await async_client.beta.threads.create_and_run(
            assistant_id="string",
        )
        assert_matches_type(Run, thread, path=["response"])

    @parametrize
    async def test_method_create_and_run_with_all_params_overload_1(self, async_client: AsyncWizkid) -> None:
        thread = await async_client.beta.threads.create_and_run(
            assistant_id="string",
            instructions="string",
            metadata={},
            model="string",
            stream=False,
            thread={
                "messages": [
                    {
                        "role": "user",
                        "content": "x",
                        "file_ids": ["string"],
                        "metadata": {},
                    },
                    {
                        "role": "user",
                        "content": "x",
                        "file_ids": ["string"],
                        "metadata": {},
                    },
                    {
                        "role": "user",
                        "content": "x",
                        "file_ids": ["string"],
                        "metadata": {},
                    },
                ],
                "metadata": {},
            },
            tools=[{"type": "code_interpreter"}, {"type": "code_interpreter"}, {"type": "code_interpreter"}],
        )
        assert_matches_type(Run, thread, path=["response"])

    @parametrize
    async def test_raw_response_create_and_run_overload_1(self, async_client: AsyncWizkid) -> None:
        response = await async_client.beta.threads.with_raw_response.create_and_run(
            assistant_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Run, thread, path=["response"])

    @parametrize
    async def test_streaming_response_create_and_run_overload_1(self, async_client: AsyncWizkid) -> None:
        async with async_client.beta.threads.with_streaming_response.create_and_run(
            assistant_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(Run, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_and_run_overload_2(self, async_client: AsyncWizkid) -> None:
        thread_stream = await async_client.beta.threads.create_and_run(
            assistant_id="string",
            stream=True,
        )
        await thread_stream.response.aclose()

    @parametrize
    async def test_method_create_and_run_with_all_params_overload_2(self, async_client: AsyncWizkid) -> None:
        thread_stream = await async_client.beta.threads.create_and_run(
            assistant_id="string",
            stream=True,
            instructions="string",
            metadata={},
            model="string",
            thread={
                "messages": [
                    {
                        "role": "user",
                        "content": "x",
                        "file_ids": ["string"],
                        "metadata": {},
                    },
                    {
                        "role": "user",
                        "content": "x",
                        "file_ids": ["string"],
                        "metadata": {},
                    },
                    {
                        "role": "user",
                        "content": "x",
                        "file_ids": ["string"],
                        "metadata": {},
                    },
                ],
                "metadata": {},
            },
            tools=[{"type": "code_interpreter"}, {"type": "code_interpreter"}, {"type": "code_interpreter"}],
        )
        await thread_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_and_run_overload_2(self, async_client: AsyncWizkid) -> None:
        response = await async_client.beta.threads.with_raw_response.create_and_run(
            assistant_id="string",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_and_run_overload_2(self, async_client: AsyncWizkid) -> None:
        async with async_client.beta.threads.with_streaming_response.create_and_run(
            assistant_id="string",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
