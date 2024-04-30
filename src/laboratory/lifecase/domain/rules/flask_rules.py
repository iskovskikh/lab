from dataclasses import dataclass

from laboratory.common.domain.rules import BusinessRule


@dataclass
class PiecesCountGreaterThanZero(BusinessRule):
    __message = 'Количество кусков во флаконе должно быть больше 0'

    piece_count: int

    def is_broken(self):
        return self.piece_count < 1


