class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a person is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when a person has an expired vaccine."""
    pass


class NotWearingMaskError(Exception):
    """Raised when a person is not wearing a mask."""
    pass
