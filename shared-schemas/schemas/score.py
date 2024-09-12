from pydantic import BaseModel


class Score(BaseModel):
    reasoning: str | None = None
    confidence: str | None = None
    value: int | None = None


class Dstf(BaseModel):
    effort: str | None = None
    effort_reasoning: str | None = None
    effort_confidence: str | None = None


class Scores(BaseModel):
    timeliness: Score = Score()
    relevance: Score = Score()
    unfamiliarity: Score = Score()
    exploitability: Score = Score()
    dstf: Dstf = Dstf()
