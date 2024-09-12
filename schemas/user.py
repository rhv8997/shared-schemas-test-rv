from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from schemas.base_model import DiscoveryBaseModel
from schemas.group import GroupSummary

id_field = Field(..., description="Unique identifier")
name_field = Field(..., description="Name")
description_field = Field(..., description="Description of cognito user group")
modified_date_field = Field(..., description="Last modification date")
modified_user_field = Field(..., description="User who performed the last modification")
created_date_field = Field(..., description="Date of creation")
created_user_field = Field(..., description="User who created the record")


class UserGroupLink(DiscoveryBaseModel):
    id: UUID


class User(DiscoveryBaseModel):
    id: UUID
    name: str | None = None
    cognito_id: UUID | None = None
    created_date: datetime
    groups: List[GroupSummary] = []  # group name
    email: EmailStr
    enabled: bool


class UserCreate(DiscoveryBaseModel):
    email: EmailStr
    groups: List[UserGroupLink] = []


class UserUpdate(BaseModel):
    name: str | None = None
    enabled: bool | None = None
    groups: List[UserGroupLink] | None = None
