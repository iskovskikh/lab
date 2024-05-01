import uuid
from typing import Optional

from django.db import models

from djangoapp.common.models import BaseValueObjectModel
from laboratory.dictionaries.domain.lifecase_defect import LifeCaseDefectId
from laboratory.lifecase.domain.value_objects import MaterialDefectVO, ReferralDefectVO


class MaterialDefectModel(BaseValueObjectModel[MaterialDefectVO]):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    defect_id = models.UUIDField()  # LifeCaseDefectId
    comment = models.TextField()

    def to_domain(self) -> MaterialDefectVO:
        item = MaterialDefectVO(
            id=LifeCaseDefectId(str(self.defect_id)),
            comment=self.comment
        )
        return item

    @staticmethod
    def from_domain(defect: MaterialDefectVO | None) -> Optional['MaterialDefectModel']:
        if defect is None:
            return None

        defect, _ = MaterialDefectModel.objects.get_or_create(
            defect_id=defect.id,
            comment=defect.comment
        )

        return defect


class ReferralDefectModel(BaseValueObjectModel[ReferralDefectVO]):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    defect_id = models.UUIDField()  # LifeCaseDefectId
    comment = models.TextField()

    def to_domain(self) -> ReferralDefectVO:
        item = ReferralDefectVO(
            id=LifeCaseDefectId(str(self.defect_id)),
            comment=self.comment
        )
        return item

    @staticmethod
    def from_domain(defect: ReferralDefectVO | None) -> Optional['ReferralDefectModel']:
        if defect is None:
            return None

        defect, _ = ReferralDefectModel.objects.get_or_create(
            defect_id=defect.id,
            comment=defect.comment
        )

        return defect
