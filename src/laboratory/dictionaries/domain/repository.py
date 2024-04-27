from laboratory.common.domain.repository import AbstractRepository
from laboratory.dictionaries.domain.flask_defect import FlaskDefect, FlaskDefectId
from laboratory.dictionaries.domain.lifecase_defect import LifeCaseDefectId, LifeCaseDefect


class AbstractLifeCaseDefectRepository(AbstractRepository[LifeCaseDefectId, LifeCaseDefect]):
    pass

class AbstractFlaskDefectRepository(AbstractRepository[FlaskDefectId, FlaskDefect]):
    pass