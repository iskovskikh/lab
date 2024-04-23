from dataclasses import dataclass

from laboratory.common.domain.entities import EntityId, Entity


class PreviousCaseId(EntityId):
    pass


@dataclass(kw_only=True)
class PreviousCase(Entity[PreviousCaseId]):
    registration_number: str
    organization_title: str
    completion_date: str
    disease_report: str
