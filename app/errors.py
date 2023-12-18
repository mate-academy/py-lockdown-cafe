class VaccineError(Exception):
    """Class for vaccine errors. Raise when visitor does not have vaccine
     or have outdated vaccine or when visitor not wearing mask"""


class NotVaccinatedError(VaccineError):
    """Raise when visitor does not have vaccine"""


class OutdatedVaccineError(VaccineError):
    """Raise when visitor have outdated vaccine"""


class NotWearingMaskError(Exception):
    """Raise when visitor not wearing mask"""
