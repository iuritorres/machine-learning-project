"""This module contains fucntions to colorize text for terminal output"""

from .colors import Colors


def colorize(text: str, color: Colors = Colors.WHITE) -> str:
    """Colorize the text with the given color"""

    if not isinstance(color, Colors):
        raise ValueError(
            colorize(
                "Invalid color, parameter color must be a value from Colors enum",
                Colors.RED,
            )
        )

    return f"{color}{text}{Colors.RESET}"
