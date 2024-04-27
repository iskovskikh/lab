from laboratory.common.infrastructure.repository import AbstractRepository
from laboratory.lifecase.domain.lifecase import LifeCase, LifeCaseId


class AbstractLifeCaseRepository(AbstractRepository[LifeCaseId, LifeCase]):
    """LifeCaseRepository interface"""

