from laboratory.common.domain.entities import EntityId, Entity


class LifeCaseDefectId(EntityId):
    pass


class LifeCaseDefect(Entity[LifeCaseDefectId]):
    title: str
    type_of_defect: str
    object_of_defect: str
    comment: str
