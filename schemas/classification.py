from enum import Enum


class ClassificationEnum(str, Enum):
    official = "OFFICIAL"
    official_sensitive = "OFFICIAL SENSITIVE"
