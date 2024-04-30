from dataclasses import dataclass

from laboratory.common.domain.entities import EntityId, Entity
from laboratory.dictionaries.domain.enums import DefectTypeChoices, DefectKindChoices


class LifeCaseDefectId(EntityId):
    pass


@dataclass(kw_only=True)
class LifeCaseDefect(Entity[LifeCaseDefectId]):
    title: str
    type: DefectTypeChoices
    kind: DefectKindChoices

    @staticmethod
    def factory(
            title,
            type,
            kind,
    ) -> 'LifeCaseDefect':
        item = LifeCaseDefect(
            id=LifeCaseDefectId.next_id(),
            title=title,
            type=type,
            kind=kind,
        )

        return item
