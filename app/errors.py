class VaccineError(Exception):
    """Parent exception for all vaccine-related issues."""
    def __init__(self, message: str = "There is an issue with"
                                      " the vaccine.") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    """Raised when a visitor is not vaccinated."""
    def __init__(self, message: str = "The user is not"
                                      " vaccinated.") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is expired."""
    def __init__(self, message: str = "The user's vaccine is"
                                      " outdated.") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
    def __init__(self, message: str = "The user is not wearing"
                                      " a mask.") -> None:
        super().__init__(message)
