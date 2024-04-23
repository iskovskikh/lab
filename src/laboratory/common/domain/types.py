from typing import TypeVar

from laboratory.common.domain.entities import Entity as EntityType, EntityId as EntityTypeId

Entity = TypeVar('Entity', bound=EntityType)
EntityId = TypeVar('EntityId', bound=EntityTypeId)
