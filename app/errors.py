class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """Raised when the visitor is not vaccinated."""
    def __init__(self, message: str = "Visitor is not vaccinated") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Raised when the vaccine is expired."""
    def __init__(self, message: str = "Visitor's vaccine is outdated") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Raised when the visitor is not wearing a mask."""
    def __init__(self, message: str = "Visitor is not wearing a mask") -> None:
        super().__init__(message)
