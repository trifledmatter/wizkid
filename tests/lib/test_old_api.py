import pytest

import wizkid
from wizkid.lib._old_api import APIRemovedInV1


def test_basic_attribute_access_works() -> None:
    for attr in dir(wizkid):
        dir(getattr(wizkid, attr))


def test_helpful_error_is_raised() -> None:
    with pytest.raises(APIRemovedInV1):
        wizkid.Completion.create()  # type: ignore

    with pytest.raises(APIRemovedInV1):
        wizkid.ChatCompletion.create()  # type: ignore
