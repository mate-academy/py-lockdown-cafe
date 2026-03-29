class VaccineError(Exception):
    """Parent class for NotVaccinatedError and OutdatedVaccineError errors"""
    pass


class NotVaccinatedError(VaccineError):
    """The error occurs if the visitor does not have a vaccine"""
    pass


class OutdatedVaccineError(VaccineError):
    """The error occurs if the vaccine already expired"""
    pass


class NotWearingMaskError(Exception):
    """The error occurs if the visitor is not wearing a mask"""
    pass
