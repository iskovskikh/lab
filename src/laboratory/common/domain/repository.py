from abc import ABC, abstractmethod
from typing import Generic

from laboratory.common.domain.types import EntityType, EntityIdType


class AbstractRepository(Generic[EntityIdType, EntityType], ABC):


    @abstractmethod
    def add(self, item: EntityType) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, id: EntityIdType) -> EntityType:
        raise NotImplementedError

    @abstractmethod
    def update(self, item: EntityType) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[EntityType]:
        raise NotImplementedError

    # @abstractmethod
    # def delete(self, id: EntityId) -> None:
    #     raise NotImplementedError
