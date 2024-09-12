from enum import Enum

from schemas.str_enum import StringEnum


class SignalStageEnum(str, Enum):
    created = "CREATED"
    pre_triage = "PRETRIAGE"
    post_triage = "POSTTRIAGE"
    ready_to_use = "READY_TO_USE"


class ConceptStageEnum(str, Enum):
    definition = "DEFINITION"
    development = "DEVELOPMENT"
    maturation = "MATURATION"
    assessment = "ASSESSMENT"
    transition = "TRANSITION"


signal_transitions = {}
for src_status in SignalStageEnum:
    for dst_status in SignalStageEnum:
        signal_transitions[f"{src_status.name}_to_{dst_status.name}"] = (
            f"{src_status.value} -> {dst_status.value}"
        )

concept_transitions = {}
for src_status in ConceptStageEnum:
    for dst_status in ConceptStageEnum:
        concept_transitions[f"{src_status.name}_to_{dst_status.name}"] = (
            f"{src_status.value} -> {dst_status.value}"
        )

ConceptStageChangeEnum = StringEnum("ConceptStageChangeEnum", concept_transitions)
SignalStageChangeEnum = StringEnum("SignalStageChangeEnum", signal_transitions)
