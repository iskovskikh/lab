import abc
from typing import TypeVar, Generic

from laboratory.common.infrastructure import repository

RepositoryType = TypeVar('RepositoryType', bound=repository.AbstractRepository)


class AbstractUnitOfWork(Generic[RepositoryType], abc.ABC):
    repository: RepositoryType

    def __enter__(self) -> 'AbstractUnitOfWork':
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
