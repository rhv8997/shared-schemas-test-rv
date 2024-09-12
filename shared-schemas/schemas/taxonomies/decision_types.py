from enum import Enum


class DecisionTypeEnum(str, Enum):
    funding_decision = "Funding Decision"
    deliverable_date = "Deliverable Date"
    collaboration_decision = "Collaboration Decision"
    gate_review_decision = "Gate Review Decision"
    stakeholder_discussion = "Stakeholder Discussion"
    subject_matter_expert_discussion = "Subject Matter Expert Discussion"
    military_judgement_discussion = "Military Judgement Discussion"
    other = "Other"
