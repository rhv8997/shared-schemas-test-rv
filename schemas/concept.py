from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.base_model import DiscoveryBaseModel
from schemas.classification import ClassificationEnum
from schemas.evidence.evidence import EvidenceRelationship, EvidenceRelationshipEnum
from schemas.link import ExternalLink, Link
from schemas.pilot import PilotSummary
from schemas.relationship import (
    ConceptConceptLink,
    ConceptConceptLinkUpdate,
    SignalConceptLink,
    SignalConceptLinkUpdate,
)
from schemas.summaries import (
    ConceptSummary,
    EvidenceSummary,
    EvidenceSummaryWithRelationship,
    SignalSummary,
)
from schemas.team import TeamSummary

from .assumption import Assumption
from .hypothesis import Hypothesis
from .image import Image
from .next_step import NextStep
from .poc import PointOfContactConcept
from .score import Scores
from .stakeholder import Stakeholders
from .taxonomies.block_types import BlockTypeEnum
from .taxonomies.decision_types import DecisionTypeEnum
from .taxonomies.priorities import PriorityEnum
from .taxonomies.stages import ConceptStageChangeEnum, ConceptStageEnum
from .taxonomies.statuses import StatusChangeEnum, StatusEnum
from .version import get_package_version

MAX_CHARS = 5_000


class SystemFields(DiscoveryBaseModel):
    version: str = get_package_version()
    legacy_source_system: str | None = None
    legacy_id: str | None = None
    created_date: int
    modified_date: int
    modified_user: str
    source_type: str
    source_system: str
    originator: str


class SystemFieldsOptional(DiscoveryBaseModel):
    version: str | None = Field(default=None)
    legacy_source_system: str | None = Field(default=None)
    legacy_id: str | None = Field(default=None)
    created_date: int | None = Field(default=None)
    modified_date: int | None = Field(default=None)
    modified_user: str | None = Field(default=None)
    source_type: str | None = Field(default=None)
    source_system: str | None = Field(default=None)
    originator: str | None = Field(default=None)


class ConceptEvidenceLink(EvidenceRelationship):
    id: UUID


class ConceptEvidenceLinkUpdate(EvidenceRelationship):
    pass


class CommonFields(DiscoveryBaseModel):
    title: str = Field(default=None, min_length=1, max_length=MAX_CHARS)
    summary: str = Field(default=None, min_length=1, max_length=MAX_CHARS)
    tagline: str = Field(
        default=None,
        min_length=1,
        max_length=MAX_CHARS,
    )
    classification: ClassificationEnum | None = None
    poc: List[PointOfContactConcept] = []
    image: Image | None = None
    status: StatusEnum | None = None
    status_update: StatusChangeEnum | None = None
    status_update_date: int | None = None
    stage: ConceptStageEnum | None = None
    stage_update: ConceptStageChangeEnum | None = None
    stage_update_date: int | None = None
    related_signals: List[SignalConceptLink] | List[SignalConceptLinkUpdate] | None = []
    why_parked: str | None = Field(default=None, max_length=MAX_CHARS)
    why_watched: str | None = Field(default=None, max_length=MAX_CHARS)
    why_exploited: str | None = Field(default=None, max_length=MAX_CHARS)
    more_information: str | None = Field(default=None, max_length=MAX_CHARS)
    why_progressed: str | None = Field(default=None, max_length=MAX_CHARS)
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
    ip_reference_number: str | None = None
    ip_owner: str | None = None


class Definition(DiscoveryBaseModel):
    # Definition#
    new_st: str | None = None
    st_insight: str | None = None
    concept_type: str | None = None
    concept_type_reasoning: str | None = None
    # Relevance&Exploitability#
    thr_or_opp: str | None = None  # radio
    thr_or_opp_explanation: str | None = None
    defence_application: List[str] = []
    eng_int_challenge: str | None = None  # radio
    eng_int_challenge_explanation: str | None = None
    # the whys#
    why_defence: str | None = None
    why_futures: str | None = None
    why_now: str | None = None
    why_interesting: str | None = None
    evidence_against_cont: str | None = None
    ###
    definition_review_reasoning: str | None = None


class Development(DiscoveryBaseModel):
    # use case and assumptions#
    use_cases_present: List[str] = []
    use_cases_future: List[str] = []
    similar_concepts: (
        List[ConceptConceptLink] | List[ConceptConceptLinkUpdate] | None
    ) = []  # multiselect
    cone_of_plausibility: str | None = None
    # relevance#
    primary_application: str | None = None  # dropdown
    secondary_application: List[str] = []  ##multiselect
    breadth_impact: str | None = None  # single choice radio
    breadth_reasoning: str | None = None
    scale_impact: str | None = None  # single choice radio
    scale_impact_reasoning: str | None = None
    defence_relevance_challenges: List[str] = []
    # exploitability#
    key_st: str | None = None
    dstf_principles: List[str] = []
    ind_drivers: str | None = None
    ind_drivers_explanation: str | None = None
    indicators_warnings: str | None = None
    current_position: str | None = None
    # transition#
    defence_research_areas: List[str] = []
    stakeholders: Stakeholders = Stakeholders()
    # delivery#
    expertise: str | None = None
    considerations: str | None = None
    ###
    development_review_reasoning: str | None = None


class Maturation(DiscoveryBaseModel):
    hypotheses: List[Hypothesis] = []

    ###
    roi: str | None = None  # radio
    roi_explanation: str | None = None
    options_next_step: NextStep = NextStep()
    recommendation: str | None = None
    # timeliness and relevance#
    tte_min: int | None = None
    tte_likely: int | None = None
    tte_max: int | None = None
    tte_explanation: str | None = None
    defence_implications: str | None = None
    # supporting information#
    plan_link: str | None = None
    ###
    maturation_review_reasoning: str | None = None


class Assessment(DiscoveryBaseModel):
    # use cases and assumptions#
    assessment_activity: List[str] = []
    test_outcome: str | None = (
        None  # Do the tests prove the hypothesis or indicate an unexpected outcome?
    )
    residual_risk: str | None = None  # radio
    residual_risk_reasoning: str | None = None
    summary_exploitable_findings: str | None = None
    spin_off_of: ConceptSummary | str | None = None
    spin_off_concepts: List[ConceptSummary] | List[str] = []
    ###
    assessment_review_reasoning: str | None = None


class Transition(DiscoveryBaseModel):
    # Impacts #
    elevator_pitch: str | None = None
    key_findings: str | None = None
    impact_now: str | None = None
    impact_not_now: str | None = None
    impact_future: str | None = None
    impact_else: str | None = None
    what_can_now: NextStep = NextStep()
    what_should_now: str | None = None
    # Exploitation #
    exploitation_plan: str | None = None
    exploitation_links: List[str] = []
    ###
    transition_review_reasoning: str | None = None


class SupportingDocuments(DiscoveryBaseModel):
    assumptions: List[Assumption] = []
    external_evidence: List[ExternalLink] = []
    evidence: List[EvidenceSummaryWithRelationship] | None = None
    other_links: List[Link] = []
    supporting_documents: List[str] = []
    other_evidence: List[str] = []
    exploitation_requirements: List[str] = []


class SupportingDocumentsCreate(DiscoveryBaseModel):
    assumptions: List[Assumption] = []
    external_evidence: List[ExternalLink] = []
    evidence: List[ConceptEvidenceLink] = []
    other_links: List[Link] = []
    supporting_documents: List[str] = []
    other_evidence: List[str] = []
    exploitation_requirements: List[str] = []


class SupportingDocumentsUpdate(DiscoveryBaseModel):
    assumptions: List[Assumption] | None = None
    external_evidence: List[ExternalLink] | None = None
    evidence: List[ConceptEvidenceLink] | None = None
    other_links: List[Link] | None = None
    supporting_documents: List[str] | None = None
    other_evidence: List[str] | None = None
    exploitation_requirements: List[str] | None = None


class ConceptCreate(CommonFields, SystemFieldsOptional):
    definition: Definition | None = Definition()
    development: Development | None = Development()
    maturation: Maturation | None = Maturation()
    assessment: Assessment | None = Assessment()
    transition: Transition | None = Transition()
    scores: Scores | None = Scores()
    supporting_documents: SupportingDocumentsCreate | None = SupportingDocumentsCreate()
    s_t_fundamentals: str | None = None
    taxonomy_classes: List[str] = []
    legacy_source_system: str | None = None
    legacy_id: str | None = None


class ConceptUpdate(CommonFields, SystemFieldsOptional):
    title: str | None = Field(default=None, min_length=1, max_length=MAX_CHARS)
    summary: str | None = Field(default=None, min_length=1, max_length=MAX_CHARS)
    tagline: str | None = Field(default=None, min_length=1, max_length=MAX_CHARS)
    poc: List[PointOfContactConcept] | None = None
    definition: Definition | None = None
    development: Development | None = None
    maturation: Maturation | None = None
    assessment: Assessment | None = None
    transition: Transition | None = None
    scores: Scores | None = None
    supporting_documents: SupportingDocumentsUpdate | None = SupportingDocumentsUpdate()
    s_t_fundamentals: str | None = None
    taxonomy_classes: List[str] | None = None


class Concept(
    SystemFields,
    CommonFields,
):
    id: str
    reference_id: str
    poc: List[PointOfContactConcept] | None = []
    definition: Definition | None = Definition()
    development: Development | None = Development()
    maturation: Maturation | None = Maturation()
    assessment: Assessment | None = Assessment()
    transition: Transition | None = Transition()
    scores: Scores | None = Scores()
    supporting_documents: SupportingDocuments | None = SupportingDocuments()
    s_t_fundamentals: str | None = None
    taxonomy_classes: List[str] = []
