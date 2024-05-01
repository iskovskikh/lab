from django.urls import path

from djangoapp.lab.api.defects import LifeCaseDefectListApi
from djangoapp.lab.api.lifecase import LifeCaseApi, LifeCaseListApi
from djangoapp.lab.api.lifecase_defect import LifeCaseSetDefectApi

urlpatterns = [
    path('defects/', LifeCaseDefectListApi.as_view()),
    path('lifecase/', LifeCaseListApi.as_view()),
    path('lifecase/<uuid:lifecase_id>/', LifeCaseApi.as_view()),
    path('lifecase/set-defect/', LifeCaseSetDefectApi.as_view()),
    # path('lifecase/<uuid:lifecase_id>/', LifeCaseApi.as_view())
]
