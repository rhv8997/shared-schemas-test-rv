from datetime import datetime
from enum import Enum
from typing import Any, Dict, List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from schemas.base_model import DiscoveryBaseModel

# Defining the fields with a default of None
id_field = Field(description="Discovery specific UUID of the feed")
name = Field(description="Name of the feed")
query = Field(
    description="The OpenSearch query that evidence must match to be included in this feed"
)
search = Field(
    description="The Discovery search that is used to generate this feed", default=None
)
archived = Field(description="Archived flag of the feed")
created_date = Field(description="Date feed was created")
created_by = Field(description="User who created feed")
modified_date = Field(description="Date feed was last modified")
modified_by = Field(description="User who last modified the feed")
favourited_by = Field(description="List of users who have favourited the feed")
categories = Field(description="List of categories related to the feed")
setfit_status_modified_date = Field(description="Date setfit status was last modified")


class SetfitStatusEnum(str, Enum):
    untrained = "UNTRAINED"
    enabled = "ENABLED"
    disabled = "DISABLED"


# The fields are not Nullable, so passing None and not providing all field values will fail
class Feed(DiscoveryBaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID = id_field
    name: str = name
    query: Dict[str, Any] = query
    search: Dict[str, Any] | None = search
    archived: bool = archived
    created_date: datetime = created_date
    created_by: str = created_by
    modified_date: datetime = modified_date
    modified_by: str = modified_by
    favourited_by: List[str] = favourited_by
    categories: List[str] = categories
    setfit_status: SetfitStatusEnum = SetfitStatusEnum.untrained
    setfit_status_modified_date: datetime = setfit_status_modified_date
    setfit_last_run: datetime | None = None
    setfit_last_run_duration: int | None = None
    setfit_first_run: datetime | None = None


class FeedEvidenceLink(DiscoveryBaseModel):
    id: UUID
    belongs: bool | None = None
    score: float | None = None


class FeedEvidenceLinkUpdate(DiscoveryBaseModel):
    belongs: bool | None = None
    score: float | None = None


# The fields are Nullable, we pass None by default, so not all values are required
class FeedPartial(DiscoveryBaseModel):
    id: UUID | None = None
    name: str | None = None
    query: Dict[str, Any] | None = None
    search: Dict[str, Any] | None = None
    archived: bool | None = None
    created_date: datetime | None = None
    created_by: str | None = None
    modified_date: datetime | None = None
    modified_by: str | None = None
    favourited_by: List[str] | None = None
    categories: List[str] | None = None


# Only the required fields for FE to load, these are not nullable
# Only name is required for create, others are generated in DB
# Feed impossible to create without search
class FeedCreate(DiscoveryBaseModel):
    name: str = name
    query: Dict[str, Any] | None = None
    search: Dict[str, Any] | None = None
    favourited_by: List[str] | None = None
    categories: List[str] | None = None


class FeedUpdate(DiscoveryBaseModel):
    name: str | None = None
    query: Dict[str, Any] | None = None
    search: Dict[str, Any] | None = None
    favourited_by: List[str] | None = None
    categories: List[str] | None = None
    setfit_status: SetfitStatusEnum | None = SetfitStatusEnum.untrained
    setfit_last_run: datetime | None = None
    setfit_last_run_duration: int | None = None
    setfit_first_run: datetime | None = None
