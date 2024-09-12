from datetime import date
from typing import List

from pydantic import BaseModel


class Author(BaseModel):
    keyname: str | None = None
    forenames: str | None = None
    suffix: str | None = None
    affiliation: List[str] | None = None


class ArxivMetadata(BaseModel):
    id: str | None = None
    created: date | None = None
    updated: date | None = None
    authors: List[Author] | None = None
    title: str | None = None
    msc_class: str | None = None
    acm_class: str | None = None
    report_no: str | None = None
    journal_ref: str | None = None
    comments: str | None = None
    abstract: str | None = None
    categories: str | None = None
    doi: str | None = None
    proxy: str | None = None
    license: str | None = None
