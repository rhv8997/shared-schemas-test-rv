from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from schemas.base_model import DiscoveryBaseModel
from schemas.evidence.metadata.metadata import ExternalMetadata


class SignalConceptRelationshipEnum(str, Enum):
    CONFIRMS = "Confirms"
    SUPPORTS = "Supports"
    RELATES_TO = "Relates to"
    DISAGREES_WITH = "Disagrees with"
    DISPUTES = "Disputes"


class SignalRelationshipOptional(DiscoveryBaseModel):
    relationship: SignalConceptRelationshipEnum | None = None
    relationship_rationale: str | None = None


class SignalRelationship(DiscoveryBaseModel):
    relationship: SignalConceptRelationshipEnum
    relationship_rationale: str


class SignalConceptLinkSummary(SignalRelationship):
    id: UUID


class SignalConceptLink(SignalConceptLinkSummary):
    title: str
    reference_id: str


class SignalConceptLinkUpdate(SignalRelationshipOptional):
    id: UUID


class ConceptRelationshipOptional(DiscoveryBaseModel):
    relationship: SignalConceptRelationshipEnum | None = None
    relationship_rationale: str | None = None


class ConceptRelationship(DiscoveryBaseModel):
    relationship: SignalConceptRelationshipEnum
    relationship_rationale: str


class ConceptConceptLinkSummary(ConceptRelationship):
    id: UUID


class ConceptConceptLink(ConceptConceptLinkSummary):
    title: str
    reference_id: str


class ConceptConceptLinkUpdate(ConceptRelationshipOptional):
    id: UUID
