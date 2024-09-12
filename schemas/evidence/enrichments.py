from datetime import datetime

from pydantic import Field

from schemas.base_model import DiscoveryBaseModel


class EnrichmentResult(DiscoveryBaseModel):
    version: str = Field(description="The version of the enrichment step")
    created_date: datetime = Field(description="Timestamp of when this step was run")


class SetfitEnrichmentResult(EnrichmentResult):
    mean_arithmetic_probability: float = Field(
        description="The average arithmetic probablility of evidence relating to this model",
        default=0,
    )
    mean_geometric_probability: float = Field(
        description="The average geometric probablility of evidence relating to this model",
        default=0,
    )
    mean_top_3_probability: float = Field(
        description="The average of the top three probabilities of chunked evidence",
        default=0,
    )


class CoeusEnrichmentResult(EnrichmentResult):
    weight: float = Field(
        description="The weight for the coeus topic",
        default=0,
    )
    coeus_display_name: str = Field(
        description="The coeus topic name",
    )
    topic_id: str = Field(description="The topic ID")
    coeus_id: str = Field(description="The coeus ID for the topic")


class ExcitementEnrichmentResult(EnrichmentResult):
    excitement_score: int = Field(
        description="Counts for instances of exciting phrases in evidence description.",
        default=0,
    )


class TruesEnrichmentResult(EnrichmentResult):
    timeliness: int | None = Field(
        default=None, description="Score for timeliness criteria"
    )
    timeliness_justification: str | None = Field(
        default=None, description="Justification for score of timeliness criteria"
    )
    relevance: int | None = Field(
        default=None, description="Score for relevance criteria"
    )
    relevance_justification: str | None = Field(
        default=None, description="Justification for score of relevance criteria"
    )
    unfamiliarity: int | None = Field(
        default=None, description="Score for unfamiliarity criteria"
    )
    unfamiliarity_justification: str | None = Field(
        default=None, description="Justification for score of unfamiliarity criteria"
    )
    exploitability: int | None = Field(
        default=None, description="Score for exploitability criteria"
    )
    exploitability_justification: str | None = Field(
        default=None, description="Justification for score of exploitability criteria"
    )
    significance: int | None = Field(
        default=None, description="Score for significance criteria"
    )
    significance_justification: str | None = Field(
        default=None, description="Justification for score of significance criteria"
    )


class Enrichments(DiscoveryBaseModel):
    setfit: list[SetfitEnrichmentResult] | None = None
    coeus: list[CoeusEnrichmentResult] | None = None
    excitement: list[ExcitementEnrichmentResult] | None = None
    trues: list[TruesEnrichmentResult] | None = None
