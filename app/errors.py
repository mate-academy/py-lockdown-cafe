class VaccineError(Exception):
    """Exception when there is problem with vaccination!"""
    pass


class NotVaccinatedError(VaccineError):
    """Exception is when there is haven't vaccination"""
    pass


class OutdatedVaccineError(VaccineError):
    """Exception when the vaccination is expired"""
    pass


class NotWearingMaskError(Exception):
    """Exception is when there is haven't mask"""
    pass
