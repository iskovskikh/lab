from drf_spectacular.utils import extend_schema
from rest_framework import status, views, serializers
from rest_framework.response import Response

from djangoapp.lab.models.lifecase import LifeCaseModel


class LifeCaseGetSerializer(serializers.Serializer):
    id = serializers.UUIDField()


class LifeCaseApi(views.APIView):
    @extend_schema(
        summary='Просмотр случая',
        description='Показывает случай',
        request=None,
        responses={status.HTTP_200_OK: LifeCaseGetSerializer},
    )
    def get(self, request, lifecase_id):
        # lifecase = get_lifecase_by_id(lifecase_id)
        lifecase = LifeCaseModel.objects.all()
        serializer = LifeCaseGetSerializer(lifecase)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
