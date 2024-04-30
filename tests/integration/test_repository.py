import pytest

from laboratory.lifecase.domain.entities.lifecase import LifeCase
from laboratory.lifecase.infrastructure.lifecase_repository import InMemoryLifeCaseRepository, \
    DjangoLifeCaseRepository
from laboratory.patient.domain.patient import PatientId
from laboratory.patient.domain.previous_case import PreviousCaseId


def test_lifecase_in_memory_repository_can_save(new_lifecase):

    repo = InMemoryLifeCaseRepository()
    repo.add(new_lifecase)

    saved_lifecase = repo.get(new_lifecase.id)

    assert saved_lifecase.id == new_lifecase.id
    assert saved_lifecase.patient_id == new_lifecase.patient_id
    assert saved_lifecase.selected_previous_cases == new_lifecase.selected_previous_cases


@pytest.mark.django_db
def test_lifecase_django_repository_can_save(new_lifecase):

    repo = DjangoLifeCaseRepository()

    repo.add(new_lifecase)
    saved_lifecase = repo.get(new_lifecase.id)

    assert saved_lifecase.id == new_lifecase.id
    assert saved_lifecase.patient_id == new_lifecase.patient_id
    assert saved_lifecase.selected_previous_cases == new_lifecase.selected_previous_cases
