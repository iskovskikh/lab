from djangoapp.lab.models.lifecase import LifeCaseModel
from laboratory.common.infrastructure.repository import DjangoGenericRepository, InMemoryGenericRepository
from laboratory.lifecase.domain.entities.lifecase import LifeCase
from laboratory.lifecase.domain.repository import AbstractLifeCaseRepository
from laboratory.lifecase.domain.value_objects import LifeCaseId


class InMemoryLifeCaseRepository(InMemoryGenericRepository, AbstractLifeCaseRepository):
    pass


class DjangoLifeCaseRepository(
    DjangoGenericRepository[LifeCaseModel, LifeCaseId, LifeCase],
    AbstractLifeCaseRepository
):
    model_class = LifeCaseModel
