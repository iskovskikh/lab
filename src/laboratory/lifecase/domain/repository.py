from laboratory.common.infrastructure.repository import AbstractRepository
from laboratory.lifecase.domain.entities.lifecase import LifeCase
from laboratory.lifecase.domain.value_objects import LifeCaseId


class AbstractLifeCaseRepository(AbstractRepository[LifeCaseId, LifeCase]):
    """LifeCaseRepository interface"""

