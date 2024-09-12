from enum import Enum
from typing import List

from pydantic import BaseModel


class Stakeholder(str, Enum):
    ADVANCED_MATERIALS = "Advanced Materials"
    ARTIFICIAL_INTELLIGENCE = "Artificial Intelligence"
    AIR_SYSTEMS = "Air Systems"
    AUTONOMY = "Autonomy"
    CBR_DEFENCE = "CBR Defence"
    COMMUNICATIONS_AND_NETWORKS = "Communications and Networks"
    CRIME_AND_POLICING = "Crime and Policing"
    CYBER_SECURITY = "Cyber Security"
    DSTF = "DSTF"
    DETERRENT_AND_SUBMARINE_SYSTEMS = "Deterrent and Submarine Systems"
    ELECTROMAGNETIC_ACTIVITIES = "Electromagnetic Activities"
    FUTURE_KINETIC_EFFECTS_AND_WEAPON_SYSTEMS = (
        "Future Kinetic Effects and Weapon Systems"
    )
    FUTURE_SENSING = "Future Sensing"
    FUTURE_WORKFORCE_AND_TRAINING = "Future Workforce and Training"
    HIGH_LEVEL_DECISION_SUPPORT = "High Level Decision Support"
    HUMAN_PERFORMANCE_AND_PROTECTION = "Human Performance and Protection"
    HYPERSONICS = "Hypersonics"
    INFLUENCE_AND_COMMAND = "Influence and Command"
    LAND_SYSTEMS = "Land Systems"
    MARITIME_SYSTEMS = "Maritime Systems"
    MISSILE_DEFENCE = "Missile Defence"
    SECURITY_SYSTEMS = "Security Systems"
    SPACE_SYSTEMS = "Space Systems"
    SPECIALIST_SYSTEMS = "Specialist Systems"
    SUPPORT_AND_SUSTAINABILITY = "Support and sustainability"
    ENGINEERING_BIOLOGY = "Engineering Biology"
    HUMAN_AUGMENTATION = "Human Augmentation"
    PULSAR = "PULSAR"
    SUPPORT_TO_OPERATIONS_AND_CRISES = "Support to Operations and Crises"


class Stakeholders(BaseModel):
    programme_lead_stakeholder: Stakeholder | None = None
    key_stakeholders: List[Stakeholder] = []
    interested_stakeholders: List[Stakeholder] = []
