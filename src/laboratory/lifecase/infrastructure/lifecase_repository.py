from djangoapp.lab.models.lifecase import LifeCaseModel
from laboratory.common.infrastructure.repository import DjangoGenericRepository, InMemoryGenericRepository
from laboratory.lifecase.domain.repository import AbstractLifeCaseRepository


class InMemoryLifeCaseRepository(InMemoryGenericRepository, AbstractLifeCaseRepository):
    pass


class DjangoLifeCaseRepository(DjangoGenericRepository, AbstractLifeCaseRepository):
    model_class = LifeCaseModel
