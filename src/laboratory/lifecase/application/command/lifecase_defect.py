from dataclasses import dataclass

from laboratory.dictionaries.domain.lifecase_defect import LifeCaseDefectId
from laboratory.dictionaries.domain.repository import AbstractLifeCaseDefectRepository
from laboratory.lifecase.domain.repository import AbstractLifeCaseRepository
from laboratory.lifecase.domain.value_objects import DefectVO, FlaskDefectVO, LifeCaseId


@dataclass
class SetLifeCaseDefectCommand:
    lifecase_id: LifeCaseId
    flasks: list[FlaskDefectVO]
    comment: str
    defect_id: LifeCaseDefectId



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

    lifecase.set_defect(defect)

    lifecase_repo.update(lifecase)
