class VaccineError(Exception):
    """Base class for vaccine-related exceptions."""
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised for visitors without a vaccine."""
    pass


class OutdatedVaccineError(VaccineError):
    """Exception raised for visitors with an expired vaccine."""
    pass


class NotWearingMaskError(Exception):
    """Exception raised for visitors not wearing a mask."""
    pass
