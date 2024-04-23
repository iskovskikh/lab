from typing import Any, TypeVar

import django.db.models

from laboratory.common.domain.repository import AbstractRepository
from laboratory.common.domain.types import Entity, EntityId

DjangoModel = TypeVar('DjangoModel', bound=django.db.models.Model)


class InMemoryGenericRepository(AbstractRepository[EntityId, Entity]):

    def __init__(self) -> None:
        super().__init__()
        self.objects: dict[Any, Any] = {}

    def add(self, item: Entity):
        self.update(item)

    def get(self, id: EntityId) -> Entity:
        return self.objects[id]

    def update(self, item: Entity):
        self.objects[item.id] = item

    def list(self) -> list[Entity]:
        return list(self.objects.items())


class DjangoGenericRepository(AbstractRepository[EntityId, Entity]):
    model_class: DjangoModel

    def add(self, item: Entity):
        self.update(item)

    def get(self, id: EntityId) -> Entity:
        return (
            self.model_class.objects.filter(id=id)
            .first()
            .to_domain()
        )

    def update(self, item: Entity):
        self.model_class.from_domain(item)

    def list(self) -> list[Entity]:
        return [b.to_domain() for b in self.model_class.objects.all()]
