from typing import Any


class VaccineError(Exception):
    """Base class for vaccine-related errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    """Raised when visitor has no vaccine."""

    def __init__(self, visitor: dict[str, Any]) -> None:
        super().__init__(f"{visitor['name']} is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    """Raised when visitor's vaccine is expired."""

    def __init__(self, visitor: dict[str, Any]) -> None:
        super().__init__(f"{visitor['name']}'s vaccine is outdated.")


class NotWearingMaskError(Exception):
    """Raised when visitor is not wearing a mask."""

    def __init__(self, visitor: dict[str, Any]) -> None:
        super().__init__(f"{visitor['name']} is not wearing a mask.")
