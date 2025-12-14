import datetime


class VaccineError(Exception):
    """Base class for vaccination-related errors."""


class NotVaccinatedError(VaccineError):
    """The visitor is unvaccinated."""
    def __init__(self) -> None:
        super().__init__("Visitor is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    """The vaccine is expired."""
    def __init__(self, expiration_date: datetime.date) -> None:
        super().__init__(f"Vaccine expired on {expiration_date}.")


class NotWearingMaskError(Exception):
    """The visitor is not wearing a mask."""
    def __init__(self) -> None:
        super().__init__("Visitor is not wearing a mask.")
