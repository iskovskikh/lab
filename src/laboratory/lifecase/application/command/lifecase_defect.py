from dataclasses import dataclass

from laboratory.dictionaries.domain.flask_defect import FlaskDefectId
from laboratory.dictionaries.domain.lifecase_defect import LifeCaseDefectId
from laboratory.lifecase.domain.flask import FlaskId
from laboratory.lifecase.domain.lifecase import LifeCaseId
from laboratory.lifecase.domain.repository import AbstractLifeCaseRepository
from laboratory.lifecase.domain.value_objects import Defect


@dataclass
class FlaskDefectsDTO:
    flask_id: FlaskId
    pieces_count_to_work: int
    defect: FlaskDefectId | None


@dataclass
class SetLifeCaseDefectCommand:
    lifecase_id: LifeCaseId
    comment: str
    flasks: list[FlaskDefectsDTO]
    defect_id: LifeCaseDefectId


@dataclass
class DefectDTO:
    lifecase: LifeCase
    comment: str
    defect: LifeCaseDefect


def set_lifecase_defect_handler(
        command: SetLifeCaseDefectCommand,
        lifecase_repo: AbstractLifeCaseRepository,
        defect_repo: AbstractLifeCaseDefectRepository
):
    ...

    lifecase = lifecase_repo.get(command.lifecase_id)
    # defect_type= defect_repo.get(command.defect_id)

    defect_type = ...

    defect = Defect(
        lifecase=lifecase,
        comment=command.comment,
        defect_type=defect_type,
        flasks=[Flask(flask_data) for flask_data in command.flasks]
    )

    lifecase.set_defect(defect)

    lifecase_repo.update(lifecase)
