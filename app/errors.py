class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when the visitor has no vaccine information."""
    def __init__(
        self,
        message: str = "Visitor is not vaccinated."
    ) -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Raised when the visitor's vaccine is expired."""
    def __init__(
        self,
        message: str = "Visitor's vaccine is outdated."
    ) -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Raised when the visitor is not wearing a mask."""
    def __init__(
        self,
        message: str = "Visitor must wear a mask."
    ) -> None:
        super().__init__(message)
