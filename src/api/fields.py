from datetime import datetime
from typing import Any, Generator, Optional, Union

from pydantic import UUID4, IPvAnyAddress


class BaseCustomType(str):
    @classmethod
    def __get_validators__(cls) -> Generator:
        yield cls.validate

    @classmethod
    def validate(cls, v: str) -> Optional[NotImplementedError]:
        raise NotImplementedError


class DateTimeField(BaseCustomType):
    @classmethod
    def validate(cls, v: str) -> Any:
        """
        Validate field value.
        Args:
            v: str = field value in format "November 30, 2022, 10:55 AM"
        Returns:
            str = datetime in format "2022-11-30 10:55:00.000000"
        """
        if not isinstance(v, str):
            return ValueError
        dt = datetime.strptime(v, '%B %d, %Y, %I:%M %p')
        return dt.strftime("%Y-%m-%d %H:%M:%S.%f")

    @classmethod
    def __modify_schema__(cls, field_schema: dict) -> None:
        field_schema.update(type="string", examples=["November 30, 2022, 10:55 AM"])


class UUIDField(str):
    """Convert UUID field to string."""
    @classmethod
    def validate(cls, v: str) -> str:
        if not UUID4(v):
            raise ValueError("Invalid uuid")
        return v

    @classmethod
    def __modify_schema__(cls, field_schema: dict) -> None:
        field_schema.update(type="string", examples=['4a33135d-8aa3-47ba-bcfd-faa297b7fb5b'])


class IPvAnyField(IPvAnyAddress):
    """Convert IP field to string."""
    @classmethod
    def validate(cls, value: Union[str, bytes, int]) -> Any:
        return str(super().validate(value))

    @classmethod
    def __modify_schema__(cls, field_schema: dict) -> None:
        field_schema.update(
            type="string",
            examples=['152.216.7.110', '684D:1111:222:3333:4444:5555:6:77']
        )
