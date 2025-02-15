# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

from .assistant_tool_param import AssistantToolParam

__all__ = ["AssistantCreateParams"]


class AssistantCreateParams(TypedDict, total=False):
    model: Required[str]
    """ID of the model to use.

    You can use the
    [List models](https://platform.wizkid.com/docs/api-reference/models/list) API to
    see all of your available models, or see our
    [Model overview](https://platform.wizkid.com/docs/models/overview) for
    descriptions of them.
    """

    description: Optional[str]
    """The description of the assistant. The maximum length is 512 characters."""

    file_ids: List[str]
    """
    A list of [file](https://platform.wizkid.com/docs/api-reference/files) IDs
    attached to this assistant. There can be a maximum of 20 files attached to the
    assistant. Files are ordered by their creation date in ascending order.
    """

    instructions: Optional[str]
    """The system instructions that the assistant uses.

    The maximum length is 32768 characters.
    """

    metadata: Optional[object]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format. Keys can be a maximum of 64 characters long and values can be
    a maxium of 512 characters long.
    """

    name: Optional[str]
    """The name of the assistant. The maximum length is 256 characters."""

    tools: Iterable[AssistantToolParam]
    """A list of tool enabled on the assistant.

    There can be a maximum of 128 tools per assistant. Tools can be of types
    `code_interpreter`, `retrieval`, or `function`.
    """
