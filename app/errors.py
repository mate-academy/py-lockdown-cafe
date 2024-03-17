class VaccineError(Exception):
    """Parent for all vaccine exceptions"""


class NotVaccinatedError(VaccineError):
    """Exception if visitor hadn't vaccinate"""


class OutdatedVaccineError(VaccineError):
    """Exception if visitor vaccination date expired"""


class NotWearingMaskError(Exception):
    """Exception if visitor not wearing mask"""
