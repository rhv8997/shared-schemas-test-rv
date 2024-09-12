from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import ConfigDict

from schemas.base_model import DiscoveryBaseModel


class Pilot(DiscoveryBaseModel):
    id: UUID
    name: str
    archived: bool
    modified_date: datetime
    modified_user: str
    created_date: datetime
    created_user: str


class PilotSummary(DiscoveryBaseModel):
    id: UUID | None = None
    name: str | None = None
    archived: bool | None = None
    modified_date: datetime | None = None
    modified_user: str | None = None
    created_date: datetime | None = None
    created_user: str | None = None


class PilotCreate(DiscoveryBaseModel):
    name: str
    modified_user: str | None = None


class PilotUpdate(DiscoveryBaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str | None = None
    modified_user: str | None = None
    archived: bool | None = None
