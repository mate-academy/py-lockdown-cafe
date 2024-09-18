class VaccineError(Exception):
    """General error for the vaccination"""


class NotVaccinatedError(VaccineError):
    """Human not vaccinated error"""


class OutdatedVaccineError(VaccineError):
    """Error when human has an outdated vaccine"""


class NotWearingMaskError(VaccineError):
    """Error when human is not wearing mask"""
