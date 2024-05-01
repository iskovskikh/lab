from drf_spectacular.utils import extend_schema
from rest_framework import status, views, generics
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from djangoapp.lab.api.serializers.lifecase import LifeCaseListSerializer, LifeCaseGetSerializer
from djangoapp.lab.queries import get_lifecase_by_id, get_all_lifecases


class LifeCaseListApi(ListModelMixin, generics.GenericAPIView):
    queryset = get_all_lifecases()
    serializer_class = LifeCaseListSerializer
    pagination_class = PageNumberPagination

    filter_backends = []

    @extend_schema(
        summary='Все случаи',
        description='Показывает случаи',
        request=None,
        responses={status.HTTP_200_OK: LifeCaseListSerializer},
    )
    def get(self, request):
        return self.list(request)


class LifeCaseApi(views.APIView):
    @extend_schema(
        summary='Просмотр случая',
        description='Показывает случай',
        request=None,
        responses={status.HTTP_200_OK: LifeCaseGetSerializer},
    )
    def get(self, request, lifecase_id):
        lifecase = get_lifecase_by_id(lifecase_id)
        serializer = LifeCaseGetSerializer(lifecase)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
