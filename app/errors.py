class VaccineError(Exception):
    """Problems with vaccine"""


class NotVaccinatedError(VaccineError):
    """Guest is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Vaccine is outdated"""


class NotWearingMaskError(Exception):
    """Guest without mask"""
