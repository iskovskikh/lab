from dataclasses import dataclass

from laboratory.common.domain.entities import Entity
from laboratory.lifecase.domain.rules.flask_rules import PiecesCountGreaterThanZero
from laboratory.lifecase.domain.value_objects import FlaskDefectVO, FlaskId


@dataclass(kw_only=True)
class Flask(Entity[FlaskId]):
    pieces_count: int
    pieces_count_to_work: int = 0
    defect: FlaskDefectVO | None = None

    @staticmethod
    def factory(pieces_count):
        Flask.check_rule(PiecesCountGreaterThanZero(pieces_count))
        item = Flask(
            id=FlaskId.next_id(),
            pieces_count=pieces_count
        )
        return item
