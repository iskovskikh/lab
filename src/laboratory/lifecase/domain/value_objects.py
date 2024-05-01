from dataclasses import dataclass

from laboratory.common.domain.entities import EntityId
from laboratory.common.domain.value_objects import ValueObject
from laboratory.dictionaries.domain.enums import DefectTypeChoices, DefectKindChoices
from laboratory.dictionaries.domain.flask_defect import FlaskDefectId
from laboratory.dictionaries.domain.lifecase_defect import LifeCaseDefectId


class FlaskId(EntityId):
    pass


class LifeCaseId(EntityId):
    pass


@dataclass(frozen=True, kw_only=True)
class FlaskDefectVO(ValueObject):
    flask_id: FlaskId
    pieces_count_to_work: int
    defect_id: FlaskDefectId | None


@dataclass(frozen=True, kw_only=True)
class DefectVO(ValueObject):
    id: LifeCaseDefectId
    title: str
    type: DefectTypeChoices
    kind: DefectKindChoices
    comment: str
    flasks: list[FlaskDefectVO]


@dataclass(frozen=True, kw_only=True)
class ReferralDefectVO(ValueObject):
    id: LifeCaseDefectId
    comment: str = ''


@dataclass(frozen=True, kw_only=True)
class MaterialDefectVO(ValueObject):
    id: LifeCaseDefectId
    comment: str = ''
