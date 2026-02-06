class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Exception raised when a visitor is not vaccinated."""
    pass


class NotWearingMaskError(Exception):
    """Exception raised when a visitor is not wearing a mask."""
    pass
