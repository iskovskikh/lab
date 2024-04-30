# pylint: disable=redefined-outer-name

import pytest

from laboratory.dictionaries.domain.enums import DefectTypeChoices, DefectKindChoices
from laboratory.dictionaries.domain.lifecase_defect import LifeCaseDefect
from laboratory.lifecase.domain.entities.flask import Flask
from laboratory.lifecase.domain.entities.lifecase import LifeCase
from laboratory.patient.domain.patient import PatientId
from laboratory.patient.domain.previous_case import PreviousCaseId


# import pytest
# import requests
#
# from requests.exceptions import RequestException
#
# from allocation import config
# import wait_for_postgres

#
# def wait_for_webapp_to_come_up():
#     deadline = time.time() + 10
#     url = config.get_api_url()
#     while time.time() < deadline:
#         try:
#             return requests.get(url)
#         except RequestException:
#             time.sleep(0.5)
#     pytest.fail("API never came up")
#
#
# @pytest.fixture
# def restart_api():
#     (Path(__file__).parent / "../src/djangoproject/manage.py").touch()
#     time.sleep(0.5)
#     wait_for_webapp_to_come_up()
#
#
# @pytest.fixture(autouse=True, scope="session")
# def wait_for_postgres_to_come_up():
#     wait_for_postgres.wait_for_postgres_to_come_up()


@pytest.fixture
def new_lifecase():
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
            Flask.factory(pieces_count=9, ),
            Flask.factory(pieces_count=9, ),
            Flask.factory(pieces_count=9, ),
        ]
    )

    return lifecase


@pytest.fixture
def new_lifecase_full_referral_defect_item():
    item = LifeCaseDefect.factory(
        title='Some Lifecase Defect title',
        type=DefectTypeChoices.FULL,
        kind=DefectKindChoices.REFERRAL,
    )

    return item
