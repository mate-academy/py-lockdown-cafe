class VaccineError(Exception):
    """Exception if there is a problem with vaccine"""


class NotVaccinatedError(VaccineError):
    """ Exception if visitor not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Exception if vaccine is outdated"""


class NotWearingMaskError(Exception):
    """Exception if not wearing a mask"""
