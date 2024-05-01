from typing import Optional

from django.db import models

from djangoapp.common.models import BaseEntityModel
from laboratory.dictionaries.domain.enums import DefectTypeChoices, DefectKindChoices
from laboratory.dictionaries.domain.lifecase_defect import LifeCaseDefect, LifeCaseDefectId


class LifeCaseDefectModel(BaseEntityModel[LifeCaseDefect]):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    kind = models.CharField(max_length=255)

    def to_domain(self) -> LifeCaseDefect:
        item = LifeCaseDefect(
            id=LifeCaseDefectId(str(self.id)),
            title=self.title,
            type=getattr(DefectTypeChoices, self.type),
            kind=getattr(DefectKindChoices, self.kind),
        )
        return item

    @staticmethod
    def from_domain(defect: LifeCaseDefect | None) -> Optional['LifeCaseDefectModel']:
        if defect is None:
            return None

        defect, _ = LifeCaseDefectModel.objects.get_or_create(
            id=defect.id,
            title=defect.title,
            type=defect.type.name,
            kind=defect.kind.name,
        )

        return defect
