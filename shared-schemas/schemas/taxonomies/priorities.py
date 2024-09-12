from enum import Enum


class PriorityEnum(str, Enum):
    unassigned = "Unassigned"
    high = "High"
    low = "Low"
