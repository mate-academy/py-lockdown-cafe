class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised for visitors who are not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Exception raised for visitors with expired vaccines."""
    pass


class NotWearingMaskError(Exception):
    """Exception raised for visitors not wearing a mask."""
    pass
