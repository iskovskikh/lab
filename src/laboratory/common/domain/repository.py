from abc import ABC, abstractmethod
from typing import Generic

from laboratory.common.domain.types import Entity, EntityId


class AbstractRepository(Generic[EntityId, Entity], ABC):


    @abstractmethod
    def add(self, item: Entity) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, id: EntityId) -> Entity:
        raise NotImplementedError

    @abstractmethod
    def update(self, item: Entity) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Entity]:
        raise NotImplementedError

    # @abstractmethod
    # def delete(self, id: EntityId) -> None:
    #     raise NotImplementedError
