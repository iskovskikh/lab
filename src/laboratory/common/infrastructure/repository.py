from typing import Any, TypeVar, Generic

from djangoapp.common.models import BaseEntityModel
from laboratory.common.domain.execeptions import DomainException
from laboratory.common.domain.repository import AbstractRepository
from laboratory.common.domain.types import EntityType, EntityIdType

DjangoModel = TypeVar('DjangoModel', bound=BaseEntityModel)


class InMemoryGenericRepository(AbstractRepository[EntityIdType, EntityType]):

    def __init__(self) -> None:
        super().__init__()
        self.objects: dict[EntityIdType, Any] = {}

    def add(self, item: EntityType):
        self.update(item)

    def get(self, id: EntityIdType) -> EntityType:
        return self.objects[id]

    def update(self, item: EntityType):
        self.objects[item.id] = item

    def list(self) -> list[EntityType]:
        return list(self.objects.values())


class DjangoGenericRepository(AbstractRepository[EntityIdType, EntityType], Generic[DjangoModel, EntityIdType, EntityType]):
    model_class: type[DjangoModel]

    def add(self, item: EntityType):
        self.update(item)

    def get(self, id: EntityIdType) -> EntityType:
        model = self.model_class.objects.filter(id=id).first()
        if model is None:
            raise DomainException(f'не нашлось модели {type(id)} с id: {id}')
        return model.to_domain()

    def update(self, item: EntityType):
        self.model_class.from_domain(item)

    def list(self) -> list[EntityType]:
        return [b.to_domain() for b in self.model_class.objects.all()]
