import pytest

from laboratory.lifecase.domain.lifecase import LifeCase
from laboratory.lifecase.infrastructure.lifecase_repository import InMemoryLifeCaseRepositoryRepository, \
    DjangoLifeCaseRepositoryRepository
from laboratory.patient.domain.patient import PatientId
from laboratory.patient.domain.previous_case import PreviousCaseId


def test_lifecase_in_memory_repository_can_save():
    previous_cases = [
        PreviousCaseId.next_id(),
        PreviousCaseId.next_id(),
        PreviousCaseId.next_id()
    ]

    lifecase = LifeCase.factory(
        cito=True,
        patient_id=PatientId.next_id(),
        selected_previous_cases=previous_cases
    )

    repo = InMemoryLifeCaseRepositoryRepository()
    repo.add(lifecase)

    saved_lifecase = repo.get(lifecase.id)

    assert saved_lifecase.id == lifecase.id
    assert saved_lifecase.patient_id == lifecase.patient_id
    assert saved_lifecase.selected_previous_cases == lifecase.selected_previous_cases


@pytest.mark.django_db
def test_lifecase_django_repository_can_save():
    previous_cases = [
        PreviousCaseId.next_id(),
        PreviousCaseId.next_id(),
        PreviousCaseId.next_id()
    ]

    lifecase = LifeCase.factory(
        cito=True,
        patient_id=PatientId.next_id(),
        selected_previous_cases=previous_cases
    )

    repo = DjangoLifeCaseRepositoryRepository()

    repo.add(lifecase)
    saved_lifecase = repo.get(lifecase.id)

    assert saved_lifecase.id == lifecase.id
    assert saved_lifecase.patient_id == lifecase.patient_id
    assert saved_lifecase.selected_previous_cases == lifecase.selected_previous_cases
