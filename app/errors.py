from datetime import date


class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a visitor is not vaccinated."""
    def __init__(self, visitor_name: str) -> None:
        super().__init__(f"Visitor {visitor_name} is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is expired."""
    def __init__(
            self,
            visitor_name: str,
            expiration_date: date | None) -> None:
        super().__init__(
            f"Visitor {visitor_name} has an outdated vaccine "
            f"(expired on {expiration_date}).")


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
    def __init__(self, visitor_name: str) -> None:
        super().__init__(f"Visitor {visitor_name} is not wearing a mask.")
