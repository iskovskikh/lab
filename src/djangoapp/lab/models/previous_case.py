from django.db import models

from djangoapp.lab.models.patient import PatientModel
from laboratory.patient.domain.previous_case import PreviousCase as PreviousCaseEntity, \
    PreviousCaseId as PreviousCaseEntityId


class PreviousCaseModel(models.Model):
    id = models.UUIDField()
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE, related_name='previous_cases')
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
    def from_domain(previous_case: PreviousCaseEntity, patient: PatientModel) -> 'PreviousCaseModel':
        item, _ = PreviousCaseModel.objects.get_or_create(
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
