# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """
    A [File](https://platform.wizkid.com/docs/api-reference/files) ID (with
    `purpose="assistants"`) that the assistant should use. Useful for tools like
    `retrieval` and `code_interpreter` that can access files.
    """
