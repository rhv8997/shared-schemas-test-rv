from decimal import Decimal

from pydantic import BaseModel


class Hypothesis(BaseModel):
    hypothesis: str | None = None
    science_impact: str | None = None
    proposed_approach: str | None = None
    cost: float | None = None
    how_long_in_months: int | None = None
    assessment_risk: str | None = None
    assessment_reasoning: str | None = None
