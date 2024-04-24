from dataclasses import dataclass, field

from laboratory.common.domain.entities import Entity, EntityId
from laboratory.patient.domain.patient import PatientId
from laboratory.patient.domain.previous_case import PreviousCaseId


class LifeCaseId(EntityId):
    pass


@dataclass(kw_only=True)
class LifeCase(Entity[LifeCaseId]):
    cito: bool = False
    patient_id: PatientId = None
    selected_previous_cases: list[PreviousCaseId] = field(default_factory=list)

    @staticmethod
    def factory(
            cito,
            patient_id,
            selected_previous_cases,
    ) -> 'LifeCase':

        LifeCase.validate_selected_previous_cases()

        lifecase = LifeCase(
            id=LifeCaseId.next_id(),
            cito=cito,
            patient_id=patient_id,
            selected_previous_cases=selected_previous_cases,
        )

        return lifecase

    @staticmethod
    def validate_selected_previous_cases():
        ...
