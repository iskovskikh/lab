from laboratory.common.domain.entities import EntityId, Entity


class FlaskDefectId(EntityId):
    pass


class FlaskDefect(Entity[FlaskDefectId]):
    title: str
    comment: str
