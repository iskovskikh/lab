from typing import TypeVar

from laboratory.common.domain.entities import Entity, EntityId
from laboratory.common.domain.value_objects import ValueObject

EntityType = TypeVar('EntityType', bound=Entity)
EntityIdType = TypeVar('EntityIdType', bound=EntityId)

ValueObjectType = TypeVar('ValueObjectType', bound=ValueObject)
