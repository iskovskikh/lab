from dataclasses import dataclass, field
from datetime import date
from uuid import UUID

from laboratory.lifecase.domain.lifecase import LifeCase
from laboratory.lifecase.domain.repository import AbstractLifeCaseRepository
from laboratory.patient.domain.repository import AbstractPatientRepository


@dataclass
class PreviousCaseDTO:
    id: UUID | None
    register_number: str
    organization_title: str
    disease_report: str
    completion_date: date | None


@dataclass
class PatientDTO:
    ipa: str
    surname: str
    name: str
    patronymic: str
    birthday: date | None
    previous_cases: list[PreviousCaseDTO] = field(default_factory=list)


@dataclass
class LifeCaseRegisterDTO:
    cito: bool
    patient: PatientDTO | None

@dataclass
class RegisterNewLifeCaseCommand:
    data: LifeCaseRegisterDTO

def register_edit_lifecase_command_handler(
    command: RegisterNewLifeCaseCommand,
    lifecase_repo: AbstractLifeCaseRepository,
    patient_repo: AbstractPatientRepository
):
    casetts = lifecase_repo.get_cassets()

    # cassetts ....


def register_new_lifecase_command_handler(
    command: RegisterNewLifeCaseCommand,
    lifecase_repo: AbstractLifeCaseRepository,
    patient_repo: AbstractPatientRepository
):

    # previous_cases = ...

    # patient = patient_repo.get_by_ipa(command.data.patient.ipa)
    # patient = PatientModel.objects.get_or_create(ipa=command.data.patient.ipa)

    # if patient is None:
    #     patient = Patient()

    # lifecase = LifeCase.factory(
    #     cito=...,
    #     patient_id=...,
    #     selected_previous_cases=previous_cases,
    # )

    # lifecase_repo.add(lifecase)

    pass