class VaccineError(Exception):
    """Parent exception for all vaccine-related issues."""
    def __init__(self, message: str = "A vaccine-related issue has"
                                      " occurred. Please ensure all"
                                      " friends are vaccinated.") -> None:
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
                                      " a mask and cannot enter.") -> None:
        super().__init__(message)
