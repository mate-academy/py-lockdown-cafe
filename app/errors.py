class VaccineError(Exception):
    """Errors vaccine"""


class NotVaccinatedError(VaccineError):
    """The visitor does not have a `vaccine"""


class OutdatedVaccineError(VaccineError):
    """Vaccine must  be expired"""


class NotWearingMaskError(Exception):
    """Must wear masks"""
