from enum import Enum


class DefectTypeChoices(Enum):
    FULL = ('FULL', 'Полный')
    PARTIAL = ('PARTIAL', 'Частичный')


class DefectKindChoices(Enum):
    MATERIAL = ('MATERIAL', 'Материал')
    REFERRAL = ('REFERRAL', 'Направление')
