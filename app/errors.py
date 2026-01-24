class VaccineError(Exception):
    """Errors raised by Vaccine"""
    pass


class NotVaccinatedError(VaccineError):
    """Error raised when a visitor is not vaccinated"""
    pass


class OutdatedVaccineError(VaccineError):
    """Error raised when a vaccine is outdated"""
    pass


class NotWearingMaskError(Exception):
    """Error raised when a wearing mask is not available or False"""
    pass
