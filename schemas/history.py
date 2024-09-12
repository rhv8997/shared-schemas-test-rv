from datetime import datetime
from typing import Any
from uuid import UUID

from schemas.base_model import DiscoveryBaseModel


class HistoryItem(DiscoveryBaseModel):
    field_name: str
    modified_date: datetime
    modified_user: str
    old_value: Any
    new_value: Any
    description: str | None


class History(DiscoveryBaseModel):
    entity_id: UUID
    items: list[HistoryItem]
