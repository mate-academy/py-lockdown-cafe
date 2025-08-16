class VaccineError(Exception):
    """Local Vaccine Error"""


class NotVaccinatedError(VaccineError):
    """Person not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Person outdated vaccine"""


class NotWearingMaskError(Exception):
    """Person not wearing mask"""
