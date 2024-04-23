import uuid
from dataclasses import dataclass, field
from typing import Generic, TypeVar


class EntityId(uuid.UUID):
    @classmethod
    def next_id(cls):
        return cls(str(uuid.uuid4()))

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value, validation_info):
        if isinstance(value, str):
            return cls(value)
        if not isinstance(value, uuid.UUID):
            raise ValueError('Invalid UUID')
        return cls(value.hex)


EntityIdType = TypeVar('EntityIdType', bound=EntityId)


@dataclass
class Entity(Generic[EntityIdType]):
    id: EntityIdType = field(hash=True)

    @classmethod
    def next_id(cls) -> EntityIdType:
        return EntityIdType.next_id()
