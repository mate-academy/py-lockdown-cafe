class VaccineError(Exception):
    """General vaccine error"""


class NotVaccinatedError(VaccineError):
    """Missing vaccine error"""


class OutdatedVaccineError(VaccineError):
    """Vaccine is present but outdated"""


class NotWearingMaskError(Exception):
    """Missing mask error"""
