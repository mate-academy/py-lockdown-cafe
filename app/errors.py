from typing import Any


class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when the visitor is not vaccinated."""
    def __init__(self) -> None:
        super().__init__("Visitor is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    """Raised when the visitor's vaccine is outdated."""
    def __init__(self, expiration_date: Any) -> None:
        super().__init__(f"Vaccine expired on {expiration_date}.")


class NotWearingMaskError(Exception):
    """Raised when the visitor is not wearing a mask."""
    def __init__(self) -> None:
        super().__init__("Visitor is not wearing a mask.")
