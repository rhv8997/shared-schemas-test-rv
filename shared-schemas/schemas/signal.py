from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.base_model import DiscoveryBaseModel
from schemas.classification import ClassificationEnum
from schemas.evidence.evidence import EvidenceRelationship
from schemas.link import ExternalLink, Link
from schemas.pilot import PilotSummary
from schemas.relationship import SignalConceptLink, SignalConceptLinkUpdate
from schemas.summaries import ConceptSummary, EvidenceSummaryWithRelationship
from schemas.team import TeamSummary

from .image import Image
from .poc import PointOfContactSignal
from .score import Scores
from .taxonomies.block_types import BlockTypeEnum
from .taxonomies.decision_types import DecisionTypeEnum
from .taxonomies.priorities import PriorityEnum
from .taxonomies.stages import SignalStageChangeEnum, SignalStageEnum
from .taxonomies.statuses import StatusChangeEnum, StatusEnum
from .version import get_package_version

MAX_CHARS = 5_000


class CommonFields(DiscoveryBaseModel):
    version: str = get_package_version()
    legacy_source_system: str | None = None
    created_date: int
    modified_date: int
    modified_user: str
    source_type: str
    source_system: str
    originator: str


class CommonFieldsOptional(DiscoveryBaseModel):
    version: str | None = Field(default=None)
    legacy_source_system: str | None = Field(default=None)
    created_date: int | None = Field(default=None)
    modified_date: int | None = Field(default=None)
    modified_user: str | None = Field(default=None)
    source_type: str | None = Field(default=None)
    source_system: str | None = Field(default=None)
    originator: str | None = Field(default=None)


class BaseSignal(DiscoveryBaseModel):
    title: str = Field(default=None, min_length=1, max_length=MAX_CHARS)
    tagline: str = Field(
        default=None,
        min_length=1,
        max_length=MAX_CHARS,
    )
    summary: str = Field(default=None, min_length=1, max_length=MAX_CHARS)
    how_found: str | None = Field(default=None, max_length=MAX_CHARS)
    classification: ClassificationEnum | None = None
    poc: List[PointOfContactSignal] = []
    image: Image | None = None
    related_concepts: List[SignalConceptLinkUpdate] = []
    status: StatusEnum | None = None
    status_update: StatusChangeEnum | None = None
    status_update_date: int | None = None
    stage: SignalStageEnum | None = None
    stage_update: SignalStageChangeEnum | None = None
    stage_update_date: int | None = None
    s_t_fundamentals: str | None = None
    taxonomy_classes: List[str] = []
    legacy_id: str | None = None
    current_issues: str | None = Field(default=None, max_length=MAX_CHARS)
    work_undertaken: str | None = Field(default=None, max_length=MAX_CHARS)
    key_findings: str | None = Field(default=None, max_length=MAX_CHARS)
    why_interesting: str | None = Field(default=None, max_length=MAX_CHARS)
    why_parked: str | None = Field(default=None, max_length=MAX_CHARS)
    why_watched: str | None = Field(default=None, max_length=MAX_CHARS)
    supporting_evidence: List[ExternalLink] = []
    other_links: List[Link] = []
    other_evidence: List[str] | None = None
    evidence: List[EvidenceSummaryWithRelationship] | None = None
    signal_type: str | None = None
    scores: Scores = Scores()
    dashboard_status: str | None = None
    owner: str | None = None
    priority: PriorityEnum | None = None
    blocked: BlockTypeEnum | None = None
    upcoming_decision_type: DecisionTypeEnum | None = None
    upcoming_decision_date: int | None = None
    sharing_approved: bool | None = None
    sharing_stance: str | None = Field(default=None, max_length=MAX_CHARS)
    archived: bool = False
    pilots: list[PilotSummary] | None = []
    team: TeamSummary | None = None


class SignalEvidenceLink(EvidenceRelationship):
    id: UUID


class SignalEvidenceLinkUpdate(EvidenceRelationship):
    pass


class SignalCreate(BaseSignal, CommonFieldsOptional):
    legacy_source_system: str | None = None
    evidence: List[SignalEvidenceLink] | None = None


class SignalUpdate(BaseSignal, CommonFieldsOptional):
    title: str | None = Field(default=None, min_length=1, max_length=MAX_CHARS)
    tagline: str | None = Field(default=None, min_length=1, max_length=MAX_CHARS)
    summary: str | None = Field(default=None, min_length=1, max_length=MAX_CHARS)
    poc: List[PointOfContactSignal] | None = None
    scores: Scores | None = None
    related_concepts: List[SignalConceptLinkUpdate] | None = None
    s_t_fundamentals: str | None = None
    taxonomy_classes: List[str] | None = None
    evidence: List[SignalEvidenceLink] | None = None


class Signal(BaseSignal, CommonFields):
    id: str
    reference_id: str
    poc: List[PointOfContactSignal] | None = []
    related_concepts: List[SignalConceptLink] | List[SignalConceptLinkUpdate] | None = (
        None
    )
