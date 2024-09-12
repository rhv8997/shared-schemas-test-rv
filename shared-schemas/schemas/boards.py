from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import ConfigDict, Field

from schemas.base_model import DiscoveryBaseModel
from schemas.summaries import EvidenceSummary

# Defining the fields with a default of None
id_field = Field(description="Discovery specific UUID of the board")
name = Field(description="Name of the board")
archived = Field(description="Archived flag of the board")
created_date = Field(description="Date board was created")
created_by = Field(description="User who created board")
modified_date = Field(description="Date board was last modified")
modified_by = Field(description="User who last modified the board")
favourited_by = Field(description="List of users who have favourited the board")
categories = Field(description="List of categories related to the board")
evidence = Field(description="List of evidence attached to the board", default=[])


# The fields are not Nullable, so passing None and not providing all field values will fail
class Board(DiscoveryBaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID = id_field
    name: str = name
    archived: bool = archived
    created_date: datetime = created_date
    created_by: str = created_by
    modified_date: datetime = modified_date
    modified_by: str = modified_by
    favourited_by: List[str] = favourited_by
    categories: List[str] = categories
    evidence: List[EvidenceSummary] = evidence


# The fields are Nullable, we pass None by default, so not all values are required
class BoardPartial(DiscoveryBaseModel):
    id: UUID | None = None
    name: str | None = None
    archived: bool | None = None
    created_date: datetime | None = None
    created_by: str | None = None
    modified_date: datetime | None = None
    modified_by: str | None = None
    favourited_by: List[str] | None = None
    categories: List[str] | None = None
    evidence: List[EvidenceSummary] | None = None


class BoardEvidenceLink(DiscoveryBaseModel):
    id: UUID
    modified_date: datetime | None = None


class BoardEvidenceLinkUpdate(DiscoveryBaseModel):
    modified_date: datetime | None = None


# Name is required for create, others are generated in DB
class BoardCreate(DiscoveryBaseModel):
    name: str = name
    favourited_by: List[str] | None = None
    categories: List[str] | None = None
    evidence: List[BoardEvidenceLink] | None = None


class BoardUpdate(DiscoveryBaseModel):
    name: str | None = None
    archived: bool | None = None
    favourited_by: List[str] | None = None
    categories: List[str] | None = None
    evidence: List[BoardEvidenceLink] | None = None
