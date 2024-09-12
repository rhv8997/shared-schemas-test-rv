from pydantic import BaseModel

from schemas.evidence.evidence import EvidenceRelationshipEnum


class Link(BaseModel):
    url: str
    label: str


class ExternalLink(Link):
    relationship: EvidenceRelationshipEnum | None = None
    relationship_rationale: str | None = None
