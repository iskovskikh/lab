from dataclasses import dataclass

from laboratory.common.domain.entities import Entity, EntityId


class FlaskId(EntityId):
    pass


class FlaskDefectVO:
    pass


@dataclass(kw_only=True)
class Flask(Entity[FlaskId]):
    pieces_count: int
    pieces_count_to_work: int
    defect: FlaskDefectVO
