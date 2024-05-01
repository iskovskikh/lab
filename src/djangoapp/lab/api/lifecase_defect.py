from drf_spectacular.utils import extend_schema
from rest_framework import views, status
from rest_framework.response import Response

from djangoapp.lab.api.serializers.lifecase import LifeCaseSetDefectSerializer
from djangoapp.lab.models.defect import ReferralDefectModel
from djangoapp.lab.models.lifecase import LifeCaseModel
from laboratory.application import app
from laboratory.lifecase.application.command.lifecase_defect import SetLifeCaseDefectCommand


class LifeCaseSetDefectApi(views.APIView):
    @extend_schema(
        summary='Добавить/обновить брак случая',
        description='Добавить/обновить брак случая',
        request=LifeCaseSetDefectSerializer,
        responses={status.HTTP_200_OK: None},
    )
    def post(self, request):
        serializer = LifeCaseSetDefectSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            # command = from_dict(data_class=SetLifeCaseDefectCommand, data=serializer.validated_data)
            command = SetLifeCaseDefectCommand(**serializer.validated_data)
            app.execute(command)

            l = LifeCaseModel.objects.all().first()
            print(l.__dict__)

            r = ReferralDefectModel.objects.all().first()
            print(r.__dict__)

            return Response(status=status.HTTP_200_OK)
