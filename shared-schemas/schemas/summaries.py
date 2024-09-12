from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import AnyHttpUrl, BaseModel, ConfigDict

from schemas.base_model import DiscoveryBaseModel
from schemas.evidence.evidence import EvidenceRelationship
from schemas.feeds import SetfitStatusEnum


class SignalSummary(DiscoveryBaseModel):
    id: UUID
    title: str


class ConceptSummary(DiscoveryBaseModel):
    id: UUID
    title: str


class EvidenceSummary(DiscoveryBaseModel):
    id: UUID
    ids: dict[str, List[str]]
    title: str
    description: str
    external_link: AnyHttpUrl
    captured_date: datetime
    authored_date: datetime


class EvidenceSummaryWithRelationship(EvidenceSummary, EvidenceRelationship):
    pass


class BoardSummary(DiscoveryBaseModel):
    id: UUID
    name: str
    categories: List[str]
    favourited_by: List[str]
    created_date: datetime
    created_by: str
    modified_date: datetime


class FeedSummary(DiscoveryBaseModel):
    id: UUID
    name: str
    favourited_by: List[str]
    categories: List[str]
    created_date: datetime
    created_by: str
    setfit_status: SetfitStatusEnum
    setfit_status_modified_date: datetime
    setfit_last_run: datetime | None
    setfit_last_run_duration: int | None
    setfit_first_run: datetime | None
