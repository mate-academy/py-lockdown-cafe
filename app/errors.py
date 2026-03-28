from datetime import date


class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str) -> None:
        message = f"{name} is not vaccinated."
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str, expiration_date: date) -> None:
        message = (
            f"{name}'s vaccine expired on {expiration_date}."
        )
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        message = f"{name} is not wearing a mask."
        super().__init__(message)
