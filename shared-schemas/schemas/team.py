from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import ConfigDict, Field

from schemas.base_model import DiscoveryBaseModel

id_field = Field(..., description="Unique identifier")
name_field = Field(..., description="Name")
archived_field = Field(..., description="Archived indication")
modified_date_field = Field(..., description="Last modification date")
modified_user_field = Field(..., description="User who performed the last modification")
created_date_field = Field(..., description="Date of creation")
created_user_field = Field(..., description="User who created the record")


class Team(DiscoveryBaseModel):
    id: UUID = id_field
    name: str = name_field
    archived: bool = archived_field
    modified_date: datetime = modified_date_field
    modified_user: str = modified_user_field
    created_date: datetime = created_date_field
    created_user: str = created_user_field


class TeamSummary(DiscoveryBaseModel):
    id: UUID = id_field
    name: str = name_field
    archived: bool = archived_field


class TeamPartial(DiscoveryBaseModel):
    id: UUID | None = id_field
    name: str | None = name_field
    archived: bool | None = archived_field
    modified_date: datetime | None = modified_date_field
    modified_user: str | None = modified_user_field
    created_date: datetime | None = created_date_field
    created_user: str | None = created_user_field


class TeamCreate(DiscoveryBaseModel):
    name: str = name_field


class TeamUpdate(DiscoveryBaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str | None = None
    archived: bool | None = None
