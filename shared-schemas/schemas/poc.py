from pydantic import BaseModel


class PointOfContact(BaseModel):
    name: str | None = None
    role: str | None = None
    email_address: str | None = None
    relationship_to_item: str | None = None


class PointOfContactSignal(PointOfContact):
    relationship_to_signal: str | None = None


class PointOfContactConcept(PointOfContact):
    relationship_to_concept: str | None = None
