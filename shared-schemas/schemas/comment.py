from datetime import datetime
from typing import Any, Dict, Type
from uuid import UUID

from pydantic import BaseModel, EmailStr, field_serializer

from schemas.base_model import DiscoveryBaseModel


class Comment(DiscoveryBaseModel):
    id: UUID
    content: str
    tags: list[str]
    modified_user: EmailStr
    modified_date: datetime
    created_user: EmailStr
    created_date: datetime
    archived: bool = False
    replies: list["Comment"] = []
    edited: bool


# Suricate update of the forward reference.
Comment.model_rebuild()


class SignalComment(Comment):
    signal_id: UUID


class ConceptComment(Comment):
    concept_id: UUID


class CreateCommentBody(BaseModel):
    content: str
    tags: list[str]
    modified_user: EmailStr | None = None


class UpdateCommentBody(BaseModel):
    content: str | None = None
    tags: list[str] | None = None
    archived: bool | None = None
    modified_user: EmailStr | None = None
