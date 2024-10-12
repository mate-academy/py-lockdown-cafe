class VaccineError(Exception):
    """Base class for vaccine-related errors."""

    def __str__(self) -> str:
        return "There was an error related to the vaccine."


class NotVaccinatedError(VaccineError):
    """Raised when visitor is not vaccinated."""
    def __str__(self) -> str:
        return "The person is not vaccinated."


class OutdatedVaccineError(VaccineError):
    """Raised when vaccine is expired."""
    def __str__(self) -> str:
        return "The vaccine is outdated."


class NotWearingMaskError(Exception):
    """Raised when visitor is not wearing a mask."""
    def __str__(self) -> str:
        return "The person is not wearing a mask."
