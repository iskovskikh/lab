from drf_spectacular.utils import extend_schema
from rest_framework import status, generics
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination

from djangoapp.lab.api.serializers.defect import LifeCaseDefectListSerializer
from djangoapp.lab.queries import get_all_lifecase_defects


class LifeCaseDefectListApi(ListModelMixin, generics.GenericAPIView):
    queryset = get_all_lifecase_defects()
    serializer_class = LifeCaseDefectListSerializer
    pagination_class = PageNumberPagination

    @extend_schema(
        summary='Все случаи',
        description='Показывает случаи',
        request=None,
        responses={status.HTTP_200_OK: LifeCaseDefectListSerializer},
    )
    def get(self, request):
        return self.list(request)
