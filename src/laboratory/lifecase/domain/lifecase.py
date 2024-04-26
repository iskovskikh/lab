from dataclasses import dataclass, field

from laboratory.common.domain.entities import Entity, EntityId
from laboratory.common.domain.value_objects import ValueObject
from laboratory.lifecase.domain.flask import Flask
from laboratory.lifecase.domain.rules import PiecesCountGreaterThanZero, FlasksCountGreaterThanZero, IsNotLastFlask
from laboratory.patient.domain.patient import PatientId
from laboratory.patient.domain.previous_case import PreviousCaseId


class LifeCaseId(EntityId):
    pass


@dataclass(frozen=True, kw_only=True)
class LifecaseDefectVO(ValueObject):
    comment: str = ''


@dataclass(frozen=True, kw_only=True)
class MaterialDefectVO(ValueObject):
    comment: str = ''


@dataclass(kw_only=True)
class LifeCase(Entity[LifeCaseId]):
    cito: bool = False
    patient_id: PatientId = None
    selected_previous_cases: list[PreviousCaseId] = field(default_factory=list)
    flasks: list[Flask] = field(default_factory=list)

    lifecase_defect: LifecaseDefectVO = None
    material_defect: MaterialDefectVO = None

    @staticmethod
    def factory(
            cito,
            patient_id,
            selected_previous_cases,
            flasks,
    ) -> 'LifeCase':
        lifecase = LifeCase(
            id=LifeCaseId.next_id(),
            cito=cito,
            patient_id=patient_id,
            selected_previous_cases=selected_previous_cases,
        )

        lifecase.check_rule(FlasksCountGreaterThanZero(flasks))

        for flask in flasks:
            lifecase.add_flask(flask)

        return lifecase

    def add_flask(self, flask: Flask):
        self.check_rule(PiecesCountGreaterThanZero(flask.pieces_count))
        self.flasks.append(flask)

    def remove_flask(self, flask: Flask):
        self.check_rule(IsNotLastFlask(self.flasks))
        self.flasks.remove(flask)

    def set_defect(self):
        pass
