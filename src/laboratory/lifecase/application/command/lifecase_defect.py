# from dataclasses import dataclass

from laboratory.common.application.command import Command
from laboratory.dictionaries.domain.lifecase_defect import LifeCaseDefectId
from laboratory.dictionaries.domain.repository import AbstractLifeCaseDefectRepository
from laboratory.lifecase.application import lifecase_module
from laboratory.lifecase.domain.repository import AbstractLifeCaseRepository
from laboratory.lifecase.domain.value_objects import DefectVO, FlaskDefectVO, LifeCaseId


class SetLifeCaseDefectCommand(Command):
    lifecase_id: LifeCaseId
    flasks: list[FlaskDefectVO]
    comment: str
    defect_id: LifeCaseDefectId


@lifecase_module.handler(SetLifeCaseDefectCommand)
def set_lifecase_defect_handler(
        command: SetLifeCaseDefectCommand,
        lifecase_repo: AbstractLifeCaseRepository,
        defect_repo: AbstractLifeCaseDefectRepository
):
    lifecase = lifecase_repo.get(command.lifecase_id)
    defect_item = defect_repo.get(command.defect_id)

    defect = DefectVO(
        id=defect_item.id,
        title=defect_item.title,
        type=defect_item.type,
        kind=defect_item.kind,
        comment=command.comment,
        flasks=command.flasks
    )

    print('lifecase_1', lifecase.referral_defect)
    lifecase.set_defect(defect)
    print('lifecase_2', lifecase.referral_defect)
    lifecase_repo.update(lifecase)

    lifecase_repo.get(lifecase.id)
    print('lifecase_3', lifecase.referral_defect)
