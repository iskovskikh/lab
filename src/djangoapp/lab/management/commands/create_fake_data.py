from django.core.management.base import BaseCommand

from laboratory.dictionaries.domain.enums import DefectTypeChoices, DefectKindChoices
from laboratory.dictionaries.domain.lifecase_defect import LifeCaseDefect
from laboratory.dictionaries.infrastructure.defects_repository import DjangoLifeCaseDefectRepository
from laboratory.lifecase.domain.entities.flask import Flask
from laboratory.lifecase.domain.entities.lifecase import LifeCase
from laboratory.lifecase.infrastructure.lifecase_repository import DjangoLifeCaseRepository
from laboratory.patient.domain.patient import PatientId
from laboratory.patient.domain.previous_case import PreviousCaseId


class Command(BaseCommand):
    help = 'Создает случаи с тестовыми данными, по умолчанию 10шт.'

    def add_arguments(self, parser):
        # https://docs.python.org/3/library/argparse.html#the-add-argument-method
        # Optional!
        parser.add_argument('--amount', type=int, help='The amount of fake data you want')
        # parser.add_argument('amount', nargs='+', type=int)

    def _call_generate(self, amount):
        previous_cases = [
            PreviousCaseId.next_id(),
            PreviousCaseId.next_id(),
            PreviousCaseId.next_id()
        ]

        lifecase = LifeCase.factory(
            cito=True,
            patient_id=PatientId.next_id(),
            selected_previous_cases=previous_cases,
            flasks=[
                Flask.factory(pieces_count=9),
            ]
        )

        defect = LifeCaseDefect.factory(
            title='Some Lifecase Defect title',
            type=DefectTypeChoices.FULL,
            kind=DefectKindChoices.REFERRAL,
        )

        lifecase_repo = DjangoLifeCaseRepository()

        lifecase_repo.add(lifecase)

        defect_repo = DjangoLifeCaseDefectRepository()
        defect_repo.add(defect)

    def handle(self, *args, **options):
        amount = options.get('amount') or 10
        self._call_generate(amount)
