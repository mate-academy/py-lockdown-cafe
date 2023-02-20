class VaccineError(Exception):
    """The exception is raised
    when there is some problems with vaccination"""


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    """The exception is raised
        when the person has no mask on it face"""
