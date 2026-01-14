class VaccineError(Exception):
    """Parent class for vaccine exception"""


class NotVaccinatedError(VaccineError):
    """Custom exception if visitor not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Custom exception if visitor has expired vaccination"""


class NotWearingMaskError(Exception):
    """Custom exception if visitor not wearing a mask"""
