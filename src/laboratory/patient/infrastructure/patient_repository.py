from djangoapp.lab.models.patient import PatientModel
from laboratory.common.infrastructure.repository import DjangoGenericRepository, InMemoryGenericRepository
from laboratory.patient.domain.repository import AbstractPatientRepository


class InMemoryPatientRepositoryRepository(InMemoryGenericRepository, AbstractPatientRepository):
    pass


class DjangoPatientRepositoryRepository(DjangoGenericRepository, AbstractPatientRepository):
    model_class = PatientModel
