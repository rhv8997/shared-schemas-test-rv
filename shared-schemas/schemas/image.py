from enum import Enum

from pydantic import BaseModel


class CopyrightEnum(str, Enum):
    internal = "INTERNAL"
    limited = "LIMITED"
    external = "EXTERNAL"


class Image(BaseModel):
    filename: str | None = None
    copyright: CopyrightEnum | None = None
    copyright_details: str | None = None
