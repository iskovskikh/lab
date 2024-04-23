from laboratory.common.infrastructure.repository import AbstractRepository
from laboratory.patient.domain.patient import Patient, PatientId
from laboratory.patient.domain.previous_case import PreviousCase, PreviousCaseId


class AbstractPreviousCaseRepository(AbstractRepository[PreviousCaseId, PreviousCase]):
    """PreviousCaseRepository interface"""
    pass


class AbstractPatientRepository(AbstractRepository[PatientId, Patient]):
    """PatientRepository interface"""

    def get_patient_by_ipa(self, ipa) -> Patient:
        ...
