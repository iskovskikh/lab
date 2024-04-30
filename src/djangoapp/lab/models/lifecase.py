import uuid

from django.db import models

from laboratory.lifecase.domain.entities.lifecase import LifeCase
from laboratory.lifecase.domain.value_objects import LifeCaseId
from laboratory.patient.domain.patient import PatientId
from laboratory.patient.domain.previous_case import PreviousCaseId


class LifeCaseModel(models.Model):
    id = models.UUIDField(primary_key=True)
    cito = models.BooleanField()
    patient_id = models.UUIDField()

    def to_domain(self) -> LifeCase:
        entity = LifeCase(
            id=LifeCaseId(str(self.id)),
            cito=self.cito,
            patient_id=PatientId(str(self.patient_id)),
            selected_previous_cases=[
                PreviousCaseId(str(model.value))
                for model in self.selected_previous_cases.all()
            ]
        )

        return entity

    @staticmethod
    def from_domain(lifecase: LifeCase) -> 'LifeCaseModel':
        model, _ = LifeCaseModel.objects.get_or_create(
            id=lifecase.id,
            defaults=dict(
                cito=lifecase.cito,
                patient_id=lifecase.patient_id
            )
        )
        model.selected_previous_cases.set(
            SelectedPreviousCaseModel.from_domain(value=case_id, lifecase=model)
            for case_id in lifecase.selected_previous_cases
        )

        return model


class SelectedPreviousCaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.UUIDField()
    lifecase = models.ForeignKey(LifeCaseModel, on_delete=models.CASCADE, related_name='selected_previous_cases')

    @staticmethod
    def from_domain(value, lifecase):
        model, _ = SelectedPreviousCaseModel.objects.get_or_create(
            value=value,
            lifecase=lifecase,
        )
        return model
