from lato import Application

from laboratory.dictionaries.infrastructure.defects_repository import DjangoLifeCaseDefectRepository
from laboratory.lifecase.application import lifecase_module
from laboratory.lifecase.infrastructure.lifecase_repository import DjangoLifeCaseRepository

app = Application(
    'My App',
    lifecase_repo=DjangoLifeCaseRepository(),
    defect_repo=DjangoLifeCaseDefectRepository()
)
app.include_submodule(lifecase_module)
