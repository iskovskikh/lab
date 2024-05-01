import pytest

from laboratory.lifecase.domain.value_objects import DefectVO
from laboratory.lifecase.infrastructure.lifecase_repository import InMemoryLifeCaseRepository, \
    DjangoLifeCaseRepository


@pytest.mark.django_db
@pytest.mark.parametrize(
    'repo',
    [
        InMemoryLifeCaseRepository(),
        DjangoLifeCaseRepository()
    ]
)
def test_lifecase_repos(repo, new_lifecase):
    repo.add(new_lifecase)

    saved_lifecase = repo.get(new_lifecase.id)

    assert saved_lifecase.id == new_lifecase.id
    assert saved_lifecase.patient_id == new_lifecase.patient_id
    assert saved_lifecase.selected_previous_cases == new_lifecase.selected_previous_cases
    assert len(saved_lifecase.flasks) == len(new_lifecase.flasks)
    assert saved_lifecase.flasks[0].id == new_lifecase.flasks[0].id


@pytest.mark.django_db
@pytest.mark.parametrize(
    'repo',
    [
        InMemoryLifeCaseRepository(),
        DjangoLifeCaseRepository()
    ]
)
def test_lifecase_repos_can_save_defects(repo, new_lifecase, new_lifecase_full_referral_defect_item):
    defect = DefectVO(
        id=new_lifecase_full_referral_defect_item.id,
        title=new_lifecase_full_referral_defect_item.title,
        type=new_lifecase_full_referral_defect_item.type,
        kind=new_lifecase_full_referral_defect_item.kind,
        comment='some test comment',
        flasks=[]
    )

    new_lifecase.set_defect(defect)

    repo.add(new_lifecase)
    saved_lifecase = repo.get(new_lifecase.id)

    assert saved_lifecase.referral_defect is not None
    assert saved_lifecase.referral_defect == new_lifecase.referral_defect
    assert saved_lifecase.material_defect is None
