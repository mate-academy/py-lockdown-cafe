class VaccineError(Exception):
    """Exception parent class if vaccine validation did not pass"""


class NotVaccinatedError(VaccineError):
    """Exception if visitor has no vaccine data"""


class OutdatedVaccineError(VaccineError):
    """Exception if visitor has outdated vaccine"""


class NotWearingMaskError(Exception):
    """Exception if visitor is not wearing a mask"""
