from dataclasses import dataclass, field

from laboratory.common.domain.entities import Entity
from laboratory.dictionaries.domain.enums import DefectKindChoices
from laboratory.lifecase.domain.entities.flask import Flask
from laboratory.lifecase.domain.value_objects import FlaskDefectVO, LifeCaseId
from laboratory.lifecase.domain.rules.lifecase_rules import FlasksCountGreaterThanZero, IsNotLastFlask
from laboratory.lifecase.domain.value_objects import DefectVO, ReferralDefectVO, MaterialDefectVO
from laboratory.patient.domain.patient import PatientId
from laboratory.patient.domain.previous_case import PreviousCaseId


@dataclass(kw_only=True)
class LifeCase(Entity[LifeCaseId]):
    cito: bool = False
    patient_id: PatientId | None = None
    selected_previous_cases: list[PreviousCaseId] = field(default_factory=list)
    flasks: list[Flask] = field(default_factory=list)

    referral_defect: ReferralDefectVO | None = None
    material_defect: MaterialDefectVO | None = None

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
        self.flasks.append(flask)

    def update_flask(self, flask: FlaskDefectVO):
        # self.check_rule(CanUpdateFlask(self.flask))
        # запретить обновлять флаконы если статус случая не подходящий
        ...

    def remove_flask(self, flask: Flask):
        self.check_rule(IsNotLastFlask(self.flasks))
        self.flasks.remove(flask)

    def set_defect(self, defect: DefectVO):

        # self.check_rule(CanSetDefect(self.lifecase))
        # запретить добавлять дефект если статус случая не подходящий

        print('DefectVO', defect)

        if defect.kind == DefectKindChoices.REFERRAL:
            self.referral_defect = ReferralDefectVO(id=defect.id, comment=defect.comment)
        else:
            self.material_defect = MaterialDefectVO(id=defect.id, comment=defect.comment)

        for flask in defect.flasks:
            self.update_flask(flask)

        # emit defect update event
