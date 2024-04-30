from dataclasses import dataclass

from laboratory.common.domain.rules import BusinessRule
from laboratory.lifecase.domain.entities.flask import Flask


@dataclass
class FlasksCountGreaterThanZero(BusinessRule):
    __message = 'Количество флаконов должно быть больше 0'

    flasks: list[Flask]

    def is_broken(self):
        return len(self.flasks) < 1


@dataclass
class IsNotLastFlask(BusinessRule):
    __message = 'Нельзя удалить последний флакон'

    flasks: list[Flask]

    def is_broken(self):
        return len(self.flasks) > 1
