from enum import Enum

from schemas.str_enum import StringEnum


class StatusEnum(str, Enum):
    active_in_progress = "ACTIVE - IN PROGRESS"
    active_eligible = "ACTIVE - ELIGIBLE"
    active_on_hold = "ACTIVE - ON HOLD"
    active_in_review = "ACTIVE - IN REVIEW"
    active_blocked = "ACTIVE - BLOCKED"
    watched = "WATCHED"
    parked = "PARKED"
    exploited = "EXPLOITED"
    deleted = "DELETED"


all_possible_status = {}
for src_status in StatusEnum:
    for dst_status in StatusEnum:
        all_possible_status[f"{src_status.name}_to_{dst_status.name}"] = (
            f"{src_status.value} -> {dst_status.value}"
        )

StatusChangeEnum = StringEnum("StatusChangeEnum", all_possible_status)
