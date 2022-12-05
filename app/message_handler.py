from typing import List

_messages: List[bytes] = []


def add_message(message: bytes) -> None:
    global _messages
    _messages.append(message)


def reset_messages() -> None:
    global _messages
    _messages = []


def get_messages() -> List[bytes]:
    global _messages
    return _messages


def pop_message() -> bytes:
    global _messages
    return _messages.pop(0)
