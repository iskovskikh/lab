import uuid

from django.db import models

from djangoapp.common.models import BaseEntityModel
from djangoapp.lab.models.lifecase import LifeCaseModel
from laboratory.patient.domain.previous_case import PreviousCase


class SelectedPreviousCaseModel(BaseEntityModel[PreviousCase]):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.UUIDField()
    lifecase = models.ForeignKey(LifeCaseModel, on_delete=models.CASCADE, related_name='selected_previous_cases')

    @staticmethod
    def from_domain(value, lifecase):  # type: ignore[override]
        model, _ = SelectedPreviousCaseModel.objects.get_or_create(
            value=value,
            lifecase=lifecase,
        )
        return model
