from typing import Protocol


class IParser(Protocol):
    def process(self, content: bytes) -> dict:
        raise NotImplementedError
