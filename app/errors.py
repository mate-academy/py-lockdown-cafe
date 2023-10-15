class VaccineError(Exception):
    pass


class NotWearingMaskError(Exception):
    """Raised when visitor isn't wearing a mask"""


class NotVaccinatedError(VaccineError):
    """Raised when visitor isn't vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Raised when visitor's vaccine is outdated"""
