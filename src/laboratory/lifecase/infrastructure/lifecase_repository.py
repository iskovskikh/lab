from djangoapp.lab.models.lifecase import LifeCaseModel
from laboratory.common.infrastructure.repository import DjangoGenericRepository, InMemoryGenericRepository
from laboratory.lifecase.domain.repository import AbstractLifeCaseRepository


class InMemoryLifeCaseRepositoryRepository(InMemoryGenericRepository, AbstractLifeCaseRepository):
    pass


class DjangoLifeCaseRepositoryRepository(DjangoGenericRepository, AbstractLifeCaseRepository):
    model_class = LifeCaseModel

    def get_cassets(self):

        return CassetModel.objects.filteer(...)
