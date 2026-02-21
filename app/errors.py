class VaccineError(Exception):
    """Base class for vaccine-related errors"""
    pass


class NotVaccinatedError(VaccineError):
    """Error when visitor is not vaccinated"""
    pass


class OutdatedVaccineError(VaccineError):
    """Error when vaccine is expired"""
    pass


class NotWearingMaskError(Exception):
    """Error when visitor is not wearing a mask"""
    pass
