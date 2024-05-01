from rest_framework import serializers

from djangoapp.common.fields import EntityIdField
from laboratory.dictionaries.domain.flask_defect import FlaskDefectId
from laboratory.dictionaries.domain.lifecase_defect import LifeCaseDefectId
from laboratory.lifecase.domain.value_objects import FlaskId, LifeCaseId


class FlaskSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    pieces_count = serializers.IntegerField()
    pieces_count_to_work = serializers.IntegerField()


class ReferralDefectSerializer(serializers.Serializer):
    defect_id = serializers.UUIDField()  # LifeCaseDefectId
    comment = serializers.CharField()


class LifeCaseListSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    cito = serializers.BooleanField()
    referral_defect = ReferralDefectSerializer()
    material_defect = ReferralDefectSerializer()
    flasks = FlaskSerializer(many=True)


class LifeCaseGetSerializer(serializers.Serializer):
    id = serializers.UUIDField()


class FlaskDefectSerializer(serializers.Serializer):
    flask_id = EntityIdField(entity_id=FlaskId)
    pieces_count_to_work = serializers.IntegerField()
    defect_id = EntityIdField(entity_id=FlaskDefectId, allow_null=True)


class LifeCaseSetDefectSerializer(serializers.Serializer):
    lifecase_id = EntityIdField(entity_id=LifeCaseId)
    flasks = FlaskDefectSerializer(many=True)
    comment = serializers.CharField()
    defect_id = EntityIdField(entity_id=LifeCaseDefectId)
