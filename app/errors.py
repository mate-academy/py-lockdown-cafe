class VaccineError(Exception):
    """Vaccine error - father class"""


class NotVaccinatedError(VaccineError):
    """Not vaccinated error"""


class OutdatedVaccineError(VaccineError):
    """Outdated vaccine error"""


class NotWearingMaskError(Exception):
    """Not wearing mask error"""
