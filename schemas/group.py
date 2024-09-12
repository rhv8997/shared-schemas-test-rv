import uuid
from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from pydantic import EmailStr, Field

from schemas.base_model import DiscoveryBaseModel
from schemas.feature import FeatureGroupLink

id_field = Field(..., description="Unique identifier")
name_field = Field(..., description="Name")
description_field = Field(..., description="Description of cognito user group")
modified_date_field = Field(..., description="Last modification date")
modified_user_field = Field(..., description="User who performed the last modification")
created_date_field = Field(..., description="Date of creation")
created_user_field = Field(..., description="User who created the record")
features_field = Field(..., description="System features this group has access to")


class GroupSummary(DiscoveryBaseModel):
    id: UUID
    name: str


class Group(DiscoveryBaseModel):
    id: UUID = id_field
    name: str = name_field
    description: str = description_field
    created_date: datetime = created_date_field
    modified_date: datetime = modified_date_field
    created_user: EmailStr = created_user_field
    modified_user: EmailStr = modified_user_field
    features: List[FeatureGroupLink] = features_field


class GroupIDs(Enum):
    ADMINS = uuid.UUID("01914c06-10d0-7b84-a958-5916eae65f99")
    CHAMPIONS = uuid.UUID("01914c06-10d0-7d63-8f12-2673fd3864a8")
    DATA_SCIENTISTS = uuid.UUID("01914c06-10d3-7f3b-9344-c9f2c2accab2")
    DEVELOPERS = uuid.UUID("01914c06-10d3-76dd-9d8b-c754614cd9f7")
    FUTURES_ANALYSTS = uuid.UUID("01914c06-10d3-71f4-a7ad-df99e3d7941e")
    GLOBAL_COLLABORATORS = uuid.UUID("01914c06-10d3-74b7-8fa1-3b2cfb63525d")
    REVIEWERS = uuid.UUID("01914c06-10d3-7a9d-9c5b-2dce6fbc231d")
    DATABASE_DOWNLOAD = uuid.UUID("01914c06-10d3-7508-bbbf-8b213863bd8a")
    EVIDENCE_HUB = uuid.UUID("01914c06-10d3-7d0c-bc67-d88703d70e8b")

    def __str__(self):
        return str(self.value)
