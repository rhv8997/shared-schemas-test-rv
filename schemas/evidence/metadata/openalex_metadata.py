from datetime import date, datetime
from typing import Dict, List, Literal, Union

from pydantic import Field

from schemas.base_model import BaseModel


class Author(BaseModel):
    id: str | None = Field(None, description="The OpenAlex ID for the author")

    display_name: str | None = Field(None, description="The display name of the author")

    orcid: str | None = Field(None, description="The ORCID for the author")


class Institution(BaseModel):
    id: str | None = Field(None, description="The OpenAlex ID for the institution")

    display_name: str | None = Field(
        None, description="The display name of the institution"
    )

    ror: str | None = Field(None, description="The ROR ID for the institution")

    country_code: str | None = Field(
        None, description="The country code of the institution"
    )

    type: str | None = Field(None, description="The type of the institution")


class Authorship(BaseModel):
    author: Author | None = Field(
        None, description="The author of the work, as a dehydrated Author object"
    )

    author_position: str | None = Field(
        None, description="The position of the author within the work's author list"
    )

    countries: List[str] | None = Field(
        None, description="List of countries associated with the author"
    )

    institutions: List[Institution] | None = Field(
        None, description="List of institutions associated with the author"
    )

    is_corresponding: bool | None = Field(
        None, description="Indicates if the author is the corresponding author"
    )

    raw_affiliation_strings: List[str] | None = Field(
        None, description="List of raw affiliation strings for the author"
    )

    raw_author_name: str | None = Field(
        None, description="The raw unformatted name of the author"
    )


class APC(BaseModel):
    value: int | None = Field(
        None, description="The value of the APC in the original currency"
    )

    currency: str | None = Field(None, description="The currency of the APC")

    provenance: str | None = Field(None, description="The source of the APC data")

    value_usd: int | None = Field(
        None, description="The value of the APC converted into USD"
    )


class Source(BaseModel):
    id: str | None = Field(None, description="The OpenAlex ID for the source")

    display_name: str | None = Field(None, description="The display name of the source")

    issn_l: str | None = Field(None, description="The ISSN-L for the source")

    issn: List[str] | None = Field(None, description="The list of ISSNs for the source")

    host_organization: str | None = Field(
        None, description="The OpenAlex ID for the host organization"
    )

    type: str | None = Field(None, description="The type of the source")


class Location(BaseModel):
    is_oa: bool | None = Field(
        None, description="Indicates if the location is Open Access"
    )

    landing_page_url: str | None = Field(
        None, description="The landing page URL for the location"
    )

    pdf_url: str | None = Field(None, description="The PDF URL for the location")

    source: Source | None = Field(None, description="The source of the location")

    license: str | None = Field(None, description="The license for the location")

    version: str | None = Field(
        None, description="The version of the work at this location"
    )

    is_accepted: bool | None = Field(
        None, description="Indicates if the version is accepted"
    )

    is_published: bool | None = Field(
        None, description="Indicates if the version is published"
    )


class Biblio(BaseModel):
    volume: str | None = Field(None, description="The volume of the work")

    issue: str | None = Field(None, description="The issue of the work")

    first_page: str | None = Field(None, description="The first page of the work")

    last_page: str | None = Field(None, description="The last page of the work")


class Concept(BaseModel):
    id: str | None = Field(None, description="The OpenAlex ID for the concept")

    wikidata: str | None = Field(None, description="The Wikidata ID for the concept")

    display_name: str | None = Field(
        None, description="The display name of the concept"
    )

    level: int | None = Field(None, description="The level of the concept")

    score: float | None = Field(
        None, description="The score of the concept in relation to the work"
    )


class Grant(BaseModel):
    funder: str | None = Field(None, description="The OpenAlex ID for the funder")

    funder_display_name: str | None = Field(
        None, description="The display name of the funder"
    )

    award_id: str | None = Field(None, description="The award ID for the grant")


class OpenAccess(BaseModel):
    is_oa: bool | None = Field(None, description="Indicates if the work is Open Access")

    oa_status: str | None = Field(
        None, description="The Open Access status of the work"
    )

    oa_url: str | None = Field(
        None, description="The best Open Access URL for the work"
    )

    any_repository_has_fulltext: bool | None = Field(
        None, description="Indicates if any repository has the full text"
    )


class Keyword(BaseModel):
    id: str | None = Field(None, description="The OpenAlex ID for the keyword")

    display_name: str | None = Field(
        None, description="The display name of the keyword"
    )

    score: float | None = Field(
        None, description="The score of the keyword in relation to the work"
    )


class SustainableDevelopmentGoal(BaseModel):
    id: str | None = Field(None, description="The OpenAlex ID for the SDG")

    display_name: str | None = Field(None, description="The display name of the SDG")

    score: float | None = Field(
        None, description="The score of the SDG in relation to the work"
    )


class TopicField(BaseModel):
    id: str | None = Field(None, description="The ID for the topic field")

    display_name: str | None = Field(
        None, description="The display name of the topic field"
    )


class MeSHTags(BaseModel):
    descriptor_ui: str | None = None
    descriptor_name: str | None = None
    qualifier_ui: str | None = None
    qualifier_name: str | None = None
    is_major_topic: bool | None = None


class Topic(BaseModel):
    id: str | None = Field(None, description="The OpenAlex ID for the topic")

    display_name: str | None = Field(None, description="The display name of the topic")

    score: float | None = Field(
        None, description="The score of the topic in relation to the work"
    )

    subfield: TopicField | None = Field(None, description="The subfield of the topic")

    field: TopicField | None = Field(None, description="The field of the topic")

    domain: TopicField | None = Field(None, description="The domain of the topic")


class OpenAlexMetadata(BaseModel):
    abstract_inverted_index: Dict[str, List[int]] | None = Field(
        None, description="The abstract of the work as an inverted index"
    )

    authorships: List[Authorship] | None = Field(
        None, description="List of authorship objects"
    )

    apc_list: APC | None = Field(
        None, description="Information about the APC list price"
    )

    apc_paid: APC | None = Field(
        None, description="Information about the actual paid APC"
    )

    best_oa_location: Location | None = Field(
        None, description="The best available open access location"
    )

    biblio: Biblio | None = Field(
        None, description="Bibliographic information about the work"
    )

    cited_by_api_url: str | None = Field(
        None, description="URL to get a list of works that cite this work"
    )

    cited_by_count: int | None = Field(
        None, description="Number of citations to this work"
    )

    concepts: List[Concept] | None = Field(
        None, description="List of concepts related to the work"
    )

    corresponding_author_ids: List[str] | None = Field(
        None, description="List of OpenAlex IDs of corresponding authors"
    )

    corresponding_institution_ids: List[str] | None = Field(
        None, description="List of OpenAlex IDs of corresponding institutions"
    )

    countries_distinct_count: int | None = Field(
        None, description="Number of distinct countries among the authorships"
    )

    counts_by_year: List[Dict[str, int]] | None = Field(
        None, description="Counts of citations by year for the last ten years"
    )

    created_date: datetime | None = Field(
        None,
        description="The date this Work object was created in the OpenAlex dataset",
    )

    display_name: str | None = Field(
        None, description="The display name/title of the work"
    )

    doi: str | None = Field(None, description="The DOI for the work")

    fulltext_origin: str | None = Field(
        None, description="Origin of the full text if searchable"
    )

    grants: List[Grant] | None = Field(
        None, description="List of grants related to this work"
    )

    has_fulltext: bool | None = Field(
        None, description="If the work's full text is searchable in OpenAlex"
    )

    id: str | None = Field(None, description="The OpenAlex ID for this work")

    ids: Dict[str, Union[str, int]] | None = Field(
        None, description="External identifiers of this work"
    )

    indexed_in: List[str] | None = Field(
        None, description="Sources in which this work is indexed"
    )

    institutions_distinct_count: int | None = Field(
        None, description="Number of distinct institutions among the authorships"
    )

    is_paratext: bool | None = Field(
        None, description="If this work is considered paratext"
    )

    is_retracted: bool | None = Field(
        None, description="If this work has been retracted"
    )

    keywords: List[Keyword] | None = Field(
        None, description="Keywords related to the work"
    )

    language: str | None = Field(None, description="The language of the work")

    license: str | None = Field(None, description="License applied to the work")

    locations: List[Location] | None = Field(
        None, description="List of locations where this work is available"
    )

    locations_count: int | None = Field(
        None, description="Number of locations for this work"
    )

    mesh: List[MeSHTags] | None = Field(None, description="List of MeSH tag objects")

    ngrams_url: str | None = Field(
        None, description="URL for n-grams associated with this work"
    )

    open_access: OpenAccess | None = Field(
        None, description="Open Access information about the work"
    )

    primary_location: Location | None = Field(
        None, description="Primary location of this work"
    )

    primary_topic: Dict[str, Union[str, float, Dict[str, Union[str, int]]]] | None = (
        Field(None, description="Top ranked topic for this work")
    )

    publication_date: datetime | None = Field(
        None, description="Date when this work was published"
    )

    publication_year: int | None = Field(
        None, description="Year when this work was published"
    )

    referenced_works: List[str] | None = Field(
        None, description="List of works that this work cites"
    )

    related_works: List[str] | None = Field(
        None, description="List of works related to this work"
    )

    sustainable_development_goals: List[SustainableDevelopmentGoal] | None = Field(
        None, description="List of SDGs relevant to this work"
    )

    topics: List[Topic] | None = Field(
        None, description="Top ranked topics for this work"
    )

    title: str | None = Field(None, description="The title of the work")

    type: str | None = Field(None, description="The type of the work")

    type_crossref: str | None = Field(
        None,
        description="Legacy type information using Crossref's controlled vocabulary",
    )

    updated_date: datetime | None = Field(
        None, description="The last time anything in this Work object changed"
    )
