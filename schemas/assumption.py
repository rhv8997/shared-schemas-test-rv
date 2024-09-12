from pydantic import BaseModel

from schemas.confidence import Confidence


class Assumption(BaseModel):
    assumption: str | None = None
    explanation: str | None = None
    activity: str | None = None
    confidence: Confidence | None = None
