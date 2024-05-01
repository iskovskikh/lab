from enum import Enum


class DefectTypeChoices(Enum):
    FULL = 'Полный'
    PARTIAL = 'Частичный'


class DefectKindChoices(Enum):
    MATERIAL = 'Материал'
    REFERRAL = 'Направление'
