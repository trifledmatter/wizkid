from .._exceptions import WizkidError

INSTRUCTIONS = """

Wizkid error:

    missing `{library}`

This feature requires additional dependencies:

    $ pip install wizkid[{extra}]

"""


def format_instructions(*, library: str, extra: str) -> str:
    return INSTRUCTIONS.format(library=library, extra=extra)


class MissingDependencyError(WizkidError):
    pass
