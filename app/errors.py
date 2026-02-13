class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a visitor has no vaccine information."""

    def __init__(self, name: str) -> None:
        msg = f"Visitor {name} is not vaccinated."
        super().__init__(msg)


class InvalidVaccineDataError(VaccineError):
    """Raised when the vaccine data structure or types are invalid."""

    def __init__(self, name: str, detail: str) -> None:
        msg = f"Visitor {name} has invalid vaccine data: {detail}."
        super().__init__(msg)


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is expired."""

    def __init__(self, name: str, expiration: object) -> None:
        msg = (
            f"Visitor {name} has an outdated vaccine "
            f"(expired on {expiration})."
        )
        super().__init__(msg)


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""

    def __init__(self, name: str) -> None:
        msg = f"Visitor {name} is not wearing a mask."
        super().__init__(msg)
