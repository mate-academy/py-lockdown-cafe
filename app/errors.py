class VaccineError(Exception):
    """Exception, when person has problems with COVID vaccine"""


class NotVaccinatedError(VaccineError):
    """Exception, if person has no vaccine"""


class OutdatedVaccineError(VaccineError):
    """Exception, if the vaccine is outdated"""


class NotWearingMaskError(Exception):
    """Exception, if person doesn't wear a mask"""
