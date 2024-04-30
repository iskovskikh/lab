import pytest

from laboratory.common.domain.execeptions import BusinessRuleException
from laboratory.lifecase.domain.entities.flask import Flask
from laboratory.lifecase.domain.entities.lifecase import LifeCase
from laboratory.lifecase.domain.rules.flask_rules import PiecesCountGreaterThanZero
from laboratory.lifecase.domain.rules.lifecase_rules import FlasksCountGreaterThanZero
from laboratory.lifecase.domain.value_objects import DefectVO, ReferralDefectVO
from laboratory.patient.domain.patient import PatientId


def test_flask_count_gt_zero():
    with pytest.raises(BusinessRuleException) as e:
        _ = LifeCase.factory(
            cito=True,
            patient_id=PatientId.next_id(),
            selected_previous_cases=[],
            flasks=[]
        )
    assert isinstance(e.value.rule, FlasksCountGreaterThanZero)


def test_pieces_count_gt_zero():
    with pytest.raises(BusinessRuleException) as e:
        _ = Flask.factory(pieces_count=0)
    assert isinstance(e.value.rule, PiecesCountGreaterThanZero)


def test_set_defect_to_lifecase(new_lifecase, new_lifecase_full_referral_defect_item):
    defect = DefectVO(
        id=new_lifecase_full_referral_defect_item.id,
        title=new_lifecase_full_referral_defect_item.title,
        type=new_lifecase_full_referral_defect_item.type,
        kind=new_lifecase_full_referral_defect_item.kind,
        comment='some test comment',
        flasks=[]
    )

    new_lifecase.set_defect(defect)

    assert new_lifecase.material_defect is None
    assert new_lifecase.referral_defect == ReferralDefectVO(id=defect.id, comment=defect.comment)
