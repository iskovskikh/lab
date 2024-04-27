from dataclasses import dataclass

from laboratory.common.domain.value_objects import ValueObject


@dataclass(frozen=True, kw_only=True)
class Defect(ValueObject):
    comment:str
    defect_type: DefectTypesChoises
    flask:list[Flask]


@dataclass(frozen=True, kw_only=True)
class ReferralDefectVO(ValueObject):
    comment: str = ''


@dataclass(frozen=True, kw_only=True)
class MaterialDefectVO(ValueObject):
    comment: str = ''
