from django.db import models

from djangoapp.common.models import BaseEntityModel
from djangoapp.lab.models.defect import MaterialDefectModel, ReferralDefectModel
from laboratory.lifecase.domain.entities.lifecase import LifeCase
from laboratory.lifecase.domain.value_objects import LifeCaseId
from laboratory.patient.domain.patient import PatientId
from laboratory.patient.domain.previous_case import PreviousCaseId


class LifeCaseModel(BaseEntityModel[LifeCase]):
    id = models.UUIDField(primary_key=True)
    cito = models.BooleanField()
    patient_id = models.UUIDField()
    # selected_previous_cases
    referral_defect = models.ForeignKey(ReferralDefectModel, on_delete=models.CASCADE, null=True)
    material_defect = models.ForeignKey(MaterialDefectModel, on_delete=models.CASCADE, null=True)
    # flasks

    def to_domain(self) -> LifeCase:
        lifecase = LifeCase(
            id=LifeCaseId(str(self.id)),
            cito=self.cito,
            patient_id=PatientId(str(self.patient_id)),
            selected_previous_cases=[
                PreviousCaseId(str(model.value))
                for model in self.selected_previous_cases.all()
            ],
            referral_defect=self.referral_defect.to_domain() if self.referral_defect else None,
            material_defect=self.material_defect.to_domain() if self.material_defect else None,
            flasks=[
                model.to_domain()
                for model in self.flasks.all()
            ]
        )

        return lifecase

    @staticmethod
    def from_domain(lifecase: LifeCase) -> 'LifeCaseModel':
        # чтобы не было circular import:
        from djangoapp.lab.models.selected_previous_case import SelectedPreviousCaseModel
        from djangoapp.lab.models.flask import FlaskModel

        lifecase_model, _ = LifeCaseModel.objects.get_or_create(
            id=lifecase.id,
            defaults=dict(
                cito=lifecase.cito,
                patient_id=lifecase.patient_id,
                referral_defect=ReferralDefectModel.from_domain(lifecase.referral_defect),
                material_defect=MaterialDefectModel.from_domain(lifecase.material_defect),
            )
        )

        # @todo почему то не сохраняет так ^
        # referral_defect = ReferralDefectModel.from_domain(lifecase.referral_defect)
        # lifecase_model.referral_defect = referral_defect

        lifecase_model.selected_previous_cases.set(
            SelectedPreviousCaseModel.from_domain(value=case_id, lifecase=lifecase_model)
            for case_id in lifecase.selected_previous_cases
        )

        lifecase_model.flasks.set(
            FlaskModel.from_domain(flask, lifecase_model)
            for flask in lifecase.flasks
        )

        lifecase_model.save()

        return lifecase_model
