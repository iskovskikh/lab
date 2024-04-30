from laboratory.dictionaries.infrastructure.defects_repository import InMemoryLifeCaseDefectRepository
from laboratory.lifecase.application.command.lifecase_defect import set_lifecase_defect_handler, \
    SetLifeCaseDefectCommand
from laboratory.lifecase.domain.value_objects import ReferralDefectVO
from laboratory.lifecase.infrastructure.lifecase_repository import InMemoryLifeCaseRepository


def test_set_full_referral_defect_to_lifecase(new_lifecase, new_lifecase_full_referral_defect_item):
    lifecase_repo = InMemoryLifeCaseRepository()
    lifecase_repo.add(new_lifecase)

    defect_repo = InMemoryLifeCaseDefectRepository()
    defect_repo.add(new_lifecase_full_referral_defect_item)

    command = SetLifeCaseDefectCommand(
        lifecase_id=new_lifecase.id,
        flasks=[],
        comment='test comment',
        defect_id=new_lifecase_full_referral_defect_item.id
    )

    set_lifecase_defect_handler(
        command=command,
        lifecase_repo=lifecase_repo,
        defect_repo=defect_repo,
    )

    lifecase = lifecase_repo.get(new_lifecase.id)

    assert lifecase.material_defect is None
    assert lifecase.referral_defect == ReferralDefectVO(
        id=new_lifecase_full_referral_defect_item.id,
        comment=command.comment
    )
