from enum import Enum


class BlockTypeEnum(str, Enum):
    none = "None"
    on_hold = "On Hold"
    blocked = "Blocked"
