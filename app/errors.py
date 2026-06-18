class VaccineError(Exception):
    """Vaccine"""


class NotVaccinatedError(VaccineError):
    """Not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Outdated vaccine"""


class NotWearingMaskError(Exception):
    """Not wearing mask"""
