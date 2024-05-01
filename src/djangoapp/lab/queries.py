from uuid import UUID

from django.shortcuts import get_object_or_404

from djangoapp.lab.models.lifecase import LifeCaseModel
from djangoapp.lab.models.lifecase_defect import LifeCaseDefectModel


def get_lifecase_by_id(id: UUID):
    return get_object_or_404(LifeCaseModel, id=id)

def get_all_lifecases():
    return LifeCaseModel.objects.all()

def get_all_lifecase_defects():
    return LifeCaseDefectModel.objects.all()