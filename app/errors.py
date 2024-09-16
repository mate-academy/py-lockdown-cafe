class VaccineError(Exception):
    """Exception is raised when there are some problems with vaccination"""


class NotWearingMaskError(Exception):
    """Exception is raised when person is not wearing a mask"""


class NotVaccinatedError(VaccineError):
    """Exception is raised when vaccination is missing"""


class OutdatedVaccineError(VaccineError):
    """Exception is raised when vaccination is outdated"""
