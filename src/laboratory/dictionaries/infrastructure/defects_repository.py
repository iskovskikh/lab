from laboratory.common.infrastructure.repository import InMemoryGenericRepository
from laboratory.dictionaries.domain.repository import AbstractLifeCaseDefectRepository, AbstractFlaskDefectRepository


class InMemoryLifeCaseDefectRepository(InMemoryGenericRepository, AbstractLifeCaseDefectRepository):
    pass


# class DjangoLifeCaseDefectRepository(DjangoGenericRepository, AbstractLifeCaseDefectRepository):
#     model_class = LifeCaseDefectModel


class InMemoryFlaskDefectRepository(InMemoryGenericRepository, AbstractFlaskDefectRepository):
    pass

# class DjangoFlaskDefectRepository(DjangoGenericRepository, AbstractFlaskDefectRepository):
#     model_class = FlaskDefectModel
