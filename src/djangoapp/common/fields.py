from typing import Generic

from rest_framework.fields import UUIDField

from laboratory.common.domain.types import EntityIdType


class EntityIdField(UUIDField):
    entity_id = None

    def __init__(self, **kwargs):
        self.entity_id = kwargs.pop('entity_id')
        super().__init__(**kwargs)

    def to_internal_value(self, data):
        return self.entity_id(str(data))
