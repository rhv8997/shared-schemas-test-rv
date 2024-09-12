from pydantic import BaseModel


class NextStep(BaseModel):
    stop: str | None = None
    transfer: str | None = None
    continue_incubate: str | None = None
    share: str | None = None
    export: str | None = None
