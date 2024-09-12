from typing import List

from schemas.base_model import DiscoveryBaseModel
from schemas.evidence.metadata.arxiv_metadata import ArxivMetadata
from schemas.evidence.metadata.feedly_metadata import FeedlyMetadata
from schemas.evidence.metadata.openalex_metadata import OpenAlexMetadata


class ExternalMetadata(DiscoveryBaseModel):
    feedly: List[FeedlyMetadata] | None = None
    openalex: List[OpenAlexMetadata] | None = None
    arxiv: List[ArxivMetadata] | None = None
