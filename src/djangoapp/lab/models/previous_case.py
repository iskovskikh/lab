from django.db import models

from djangoapp.common.models import BaseEntityModel
from djangoapp.lab.models.patient import PatientEntityModel
from laboratory.patient.domain.previous_case import PreviousCase as PreviousCaseEntity, \
    PreviousCaseId as PreviousCaseEntityId


class PreviousCaseEntityModel(BaseEntityModel[PreviousCaseEntity]):
    id = models.UUIDField()
    patient = models.ForeignKey(PatientEntityModel, on_delete=models.CASCADE, related_name='previous_cases')
    registration_number = models.CharField(max_length=255)
    organization_title = models.CharField(max_length=255)
    completion_date = models.CharField(max_length=255)
    disease_report = models.CharField(max_length=255)

    def to_domain(self) -> PreviousCaseEntity:
        previous_case = PreviousCaseEntity(
            id=PreviousCaseEntityId(str(self.id)),
            registration_number=self.registration_number,
            organization_title=self.organization_title,
            completion_date=self.completion_date,
            disease_report=self.disease_report
        )

        return previous_case

    @staticmethod
    def from_domain(previous_case: PreviousCaseEntity, patient: PatientEntityModel) -> 'PreviousCaseEntityModel':
        item, _ = PreviousCaseEntityModel.objects.get_or_create(
            id=previous_case.id,
            defaults=dict(
                patient=patient,
                registration_number=previous_case.registration_number,
                organization_title=previous_case.organization_title,
                completion_date=previous_case.completion_date,
                disease_report=previous_case.disease_report
            )
        )
        return item
