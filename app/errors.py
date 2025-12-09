class VaccineError(Exception):
    """Error if client have a problem with vaccine"""


class NotVaccinatedError(VaccineError):
    """Error if client do not have vaccine"""


class OutdatedVaccineError(VaccineError):
    """Error if vaccine is outdated"""


class NotWearingMaskError(Exception):
    """Error if client do not have wearing mask"""
