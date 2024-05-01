from rest_framework import serializers


class LifeCaseDefectListSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    type = serializers.CharField()
    kind = serializers.CharField()