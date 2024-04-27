from dataclasses import dataclass
from datetime import date

from laboratory.common.domain.entities import Entity, EntityId
from laboratory.patient.domain.previous_case import PreviousCase, PreviousCaseId


class PatientId(EntityId):
    pass


@dataclass(kw_only=True)
class Patient(Entity[PatientId]):
    surname: str
    name: str
    patronymic: str
    birthday: date
    previous_cases: list[PreviousCase]

    @staticmethod
    def factory(
            surname: str,
            name: str,
            patronymic: str,
            birthday: date,
            previous_cases: list,
    ) -> 'Patient':
        patient = Patient(
            id=PatientId.next_id(),
            surname=surname,
            name=name,
            patronymic=patronymic,
            birthday=birthday,
            previous_cases=previous_cases
        )

        return patient



    def update_patient(self, data):
        ...

    def get_previous_case_by_id(self, id: PreviousCaseId) -> PreviousCase:
        ...

    def add_previous_case(self, previous_case: PreviousCase):
        ...

    def update_previous_case(self, previous_case: PreviousCase):
        ...