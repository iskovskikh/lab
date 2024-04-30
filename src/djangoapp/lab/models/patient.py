from django.db import models

from djangoapp.lab.models.previous_case import PreviousCaseModel
from laboratory.patient.domain.patient import (
    Patient as PatientEntity,
    PatientId as PatientEntityId,
)


class PatientModel(models.Model):
    id = models.UUIDField()
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    birthday = models.DateField()

    def to_domain(self) -> PatientEntity:
        patient = PatientEntity(
            id=PatientEntityId(str(self.id)),
            surname=self.surname,
            name=self.name,
            patronymic=self.patronymic,
            birthday=self.birthday,
            previous_cases=list(
                items.to_domain() for items in self.previous_cases.all()
            )
        )
        return patient

    @staticmethod
    def from_domain(patient: PatientEntity):
        item = PatientModel.objects.get_or_create(
            id=patient.id,
            defaults=dict(
                name=patient.name,
                surname=patient.surname,
                patronymic=patient.patronymic,
                birthday=patient.birthday,
            )
        )

        item.save()

        item.previous_cases.set(
            PreviousCaseModel.from_domain(prev_case, item) for prev_case in patient.previous_cases
        )
