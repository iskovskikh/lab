from dataclasses import dataclass

from laboratory.lifecase.domain.flask import FlaskId
from laboratory.lifecase.domain.lifecase import LifeCaseId
from laboratory.lifecase.domain.repository import AbstractLifeCaseRepository


@dataclass
class FlaskDefectsDTO:
    flask_id: FlaskId
    pieces_count_to_work: int
    info_about_defect: ...  # defect_type


@dataclass
class SetLifeCaseDefectCommand:
    lifecase_id: LifeCaseId
    flasks: list[FlaskDefectsDTO]


def set_lifecase_defect_handler(
        command: SetLifeCaseDefectCommand,
        lifecase_repo: AbstractLifeCaseRepository
):
    ...

    lifecase = lifecase_repo.get(command.lifecase_id)

    lifecase.set_defect()

    lifecase_repo.update(lifecase)