import uuid
from enum import Enum
from typing import List
from uuid import UUID

from pydantic import Field

from schemas.base_model import DiscoveryBaseModel

id_field = Field(..., description="Unique identifier of this feature")
name_field = Field(..., description="Name")


class FeatureGroupAccessEnum(str, Enum):
    member = "MEMBER"
    admin = "ADMIN"


class FeatureSummary(DiscoveryBaseModel):
    id: UUID = Field(
        ..., description="Unique identifier of the linked feature or group"
    )
    name: str = Field(..., description="Name of the linked feature or group")


class FeatureGroupLink(DiscoveryBaseModel):
    id: UUID = Field(
        ..., description="Unique identifier of the linked feature or group"
    )
    name: str | None = Field(None, description="Name of the linked feature or group")
    access: FeatureGroupAccessEnum = Field(
        ..., description="Level of access the linked group has to the feature"
    )


class Feature(DiscoveryBaseModel):
    id: UUID = id_field
    name: str = name_field
    groups: List[FeatureGroupLink]


class FeatureCreate(DiscoveryBaseModel):
    name: str = name_field
    groups: List[FeatureGroupLink]


class FeatureGroupLinkUpdate(DiscoveryBaseModel):
    group_id: UUID
    access: FeatureGroupAccessEnum


class FeatureIDs(Enum):
    WORKBENCH = uuid.UUID("01914c06-10d3-728d-b06c-38e7bf62963c")
    DATABASE_DOWNLOAD = uuid.UUID("01914c06-10d3-7159-97be-583b58e2115d")
    EVIDENCE_HUB = uuid.UUID("01914c06-10d3-763b-b10a-4d5c275f1766")
    SIGNAL_HISTORY = uuid.UUID("01914c06-10d3-7478-b1a9-ec0486a4bce9")
    CONCEPT_HISTORY = uuid.UUID("01914c06-10d3-7e2d-97c9-7a0463bc3628")
    DEVELOPER_TOKEN = uuid.UUID("01914c06-10d3-7a9c-a8ae-d2a63c38ba67")
    ADMIN_PANEL = uuid.UUID("01914c06-10d3-7cea-b05f-90670ea9ea83")
