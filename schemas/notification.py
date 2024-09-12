from datetime import datetime
from uuid import UUID

from pydantic import EmailStr, Field

from schemas.base_model import DiscoveryBaseModel

id_field = Field(description="Internal ID of this notification")
user_field = Field(description="Email of the target user")
content_field = Field(description="The message of this notification")
created_field = Field(description="When this notification was created")
archived_field = Field(
    description="If this notification has been archived", default=False
)
read_field = Field(description="If this notification has been read", default=False)


class Notification(DiscoveryBaseModel):
    id: UUID = id_field
    user: EmailStr = user_field
    content: str = content_field
    created_date: datetime = created_field
    archived: bool = archived_field
    read: bool = read_field


class NotificationPartial(DiscoveryBaseModel):
    id: UUID | None = None
    user: EmailStr | None = None
    content: str | None = None
    created_date: datetime | None = None
    archived: bool | None = None
    read: bool | None = None


class NotificationSummary(DiscoveryBaseModel):
    id: UUID = id_field
    user: EmailStr = user_field
    content: str = content_field
    created_date: datetime = created_field
    archived: bool = archived_field
    read: bool = read_field


class NotificationCreate(DiscoveryBaseModel):
    user: EmailStr = user_field
    content: str = content_field
