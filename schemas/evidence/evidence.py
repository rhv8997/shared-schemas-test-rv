from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from pydantic import AnyHttpUrl, Field

from schemas.base_model import DiscoveryBaseModel
from schemas.evidence.metadata.metadata import ExternalMetadata

from .enrichments import Enrichments

id_field: UUID = Field(description="Discovery specific UUID of this object")
ids_field: dict[str : List[str]] = Field(
    description="A list of all the external identifiers that we know about for this piece of evidence"
)

title_field: str = Field(description="The title of this object")
description_field: str = Field(description="A description of this object")
external_link_field: str = Field(
    description="A link to the best external version of this piece of evidence"
)

captured_date_field: datetime = Field(
    description="Timestamp representing when we first recieved information about this evidence"
)
authored_date_field: str = Field(
    description="Timestamp representing when the evidence was created or released"
)
enrichments_field: list[Enrichments] = Field(
    description="A dictionary of enrichment results", default={}
)

metadata_field: ExternalMetadata = Field(
    description="Any external metadata attached to this evidence",
    default=ExternalMetadata(feedly=None, openalex=None),
)
feeds_field: list[UUID] = Field(
    description="Feeds this evidence is a member of",
    default=[],
)
boards_field: list[UUID] = Field(
    description="Boards this evidence is a member of",
    default=[],
)
signals_field: list[UUID] = Field(
    description="Signals this evidence is a member of",
    default=[],
)
concepts_field: list[UUID] = Field(
    description="Concepts this evidence is a member of",
    default=[],
)


class EvidenceRelationshipEnum(str, Enum):
    CONFIRMS = "Confirms"
    SUPPORTS = "Supports"
    RELATES_TO = "Relates to"
    DISAGREES_WITH = "Disagrees with"
    DISPUTES = "Disputes"


class EvidenceRelationshipPartial(DiscoveryBaseModel):
    relationship: EvidenceRelationshipEnum | None = None
    relationship_rationale: str | None = None
    label: str | None = None


class EvidenceRelationship(DiscoveryBaseModel):
    relationship: EvidenceRelationshipEnum
    relationship_rationale: str
    label: str


class EvidenceFeedLink(DiscoveryBaseModel):
    id: UUID
    belongs: bool | None = None
    score: float | None = None


class EvidenceSignalLinkPartial(EvidenceRelationshipPartial):
    id: UUID


class EvidenceBoardLinkPartial(DiscoveryBaseModel):
    id: UUID
    modified_date: datetime | None = None


class EvidenceConceptLinkPartial(EvidenceRelationshipPartial):
    id: UUID


class EvidenceSignalLink(EvidenceSignalLinkPartial):
    title: str
    reference_id: str


class EvidenceBoardLink(EvidenceBoardLinkPartial):
    name: str


class EvidenceConceptLink(EvidenceConceptLinkPartial):
    title: str
    reference_id: str


class Evidence(DiscoveryBaseModel):
    id: UUID = id_field
    ids: dict[str, List[str]] = ids_field
    title: str = title_field
    description: str = description_field

    external_link: AnyHttpUrl = external_link_field

    captured_date: datetime = captured_date_field
    authored_date: int = authored_date_field

    external_metadata: ExternalMetadata = metadata_field

    enrichments: Enrichments = enrichments_field

    boards: list[EvidenceBoardLink] = boards_field
    feeds: list[EvidenceFeedLink] = feeds_field
    signals: list[EvidenceSignalLink] = signals_field
    concepts: list[EvidenceConceptLink] = concepts_field


class EvidencePartial(DiscoveryBaseModel):
    id: UUID | None = None
    ids: dict[str, List[str]] | None = None
    title: str | None = None
    description: str | None = None

    external_link: AnyHttpUrl | None = None

    captured_date: datetime | None = None
    authored_date: int | None = None

    external_metadata: ExternalMetadata | None = None

    enrichments: Enrichments | None = None

    boards: list[EvidenceBoardLinkPartial] | None = None
    feeds: list[EvidenceFeedLink] | None = None
    signals: list[EvidenceSignalLinkPartial] | None = None
    concepts: list[EvidenceConceptLinkPartial] | None = None


class EvidenceCreate(DiscoveryBaseModel):
    ids: dict[str, List[str]] = ids_field
    title: str = title_field
    description: str = description_field

    external_link: AnyHttpUrl = external_link_field

    authored_date: int = authored_date_field

    external_metadata: ExternalMetadata = metadata_field


class EvidenceUpdate(DiscoveryBaseModel):
    ids: dict[str, List[str]] | None = None
    title: str | None = None
    description: str | None = None
    external_link: AnyHttpUrl | None = None

    authored_date: int | None = None

    external_metadata: ExternalMetadata | None = None
