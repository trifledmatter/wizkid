# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .message_content import MessageContent

__all__ = ["Message", "IncompleteDetails"]


class IncompleteDetails(BaseModel):
    reason: Literal["content_filter", "max_tokens", "run_cancelled", "run_expired", "run_failed"]
    """The reason the message is incomplete."""


class Message(BaseModel):
    id: str
    """The identifier, which can be referenced in API endpoints."""

    assistant_id: Optional[str] = None
    """
    If applicable, the ID of the
    [assistant](https://platform.wizkid.com/docs/api-reference/assistants) that
    authored this message.
    """

    completed_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the message was completed."""

    content: List[MessageContent]
    """The content of the message in array of text and/or images."""

    created_at: int
    """The Unix timestamp (in seconds) for when the message was created."""

    file_ids: List[str]
    """
    A list of [file](https://platform.wizkid.com/docs/api-reference/files) IDs that
    the assistant should use. Useful for tools like retrieval and code_interpreter
    that can access files. A maximum of 10 files can be attached to a message.
    """

    incomplete_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the message was marked as incomplete."""

    incomplete_details: Optional[IncompleteDetails] = None
    """On an incomplete message, details about why the message is incomplete."""

    metadata: Optional[object] = None
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format. Keys can be a maximum of 64 characters long and values can be
    a maxium of 512 characters long.
    """

    object: Literal["thread.message"]
    """The object type, which is always `thread.message`."""

    role: Literal["user", "assistant"]
    """The entity that produced the message. One of `user` or `assistant`."""

    run_id: Optional[str] = None
    """
    If applicable, the ID of the
    [run](https://platform.wizkid.com/docs/api-reference/runs) associated with the
    authoring of this message.
    """

    status: Literal["in_progress", "incomplete", "completed"]
    """
    The status of the message, which can be either `in_progress`, `incomplete`, or
    `completed`.
    """

    thread_id: str
    """
    The [thread](https://platform.wizkid.com/docs/api-reference/threads) ID that
    this message belongs to.
    """
