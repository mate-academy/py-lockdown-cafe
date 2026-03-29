import datetime


class VaccineError(Exception):
    """Base class for vaccine-related exceptions."""
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor is not vaccinated."""
    def __init__(self, visitor_name: str) -> None:
        super().__init__(f"{visitor_name} is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    """Exception raised when a visitor's vaccine is expired."""
    def __init__(self, visitor_name: str,
                 expiration_date: datetime.date) -> None:
        super().__init__(
            f"{visitor_name}'s vaccine expired on "
            f"{expiration_date.strftime('%Y-%m-%d')}."
        )


class NotWearingMaskError(Exception):
    """Exception raised when a visitor is not wearing a mask."""
    def __init__(self, visitor_name: str) -> None:
        super().__init__(f"{visitor_name} is not wearing a mask.")
