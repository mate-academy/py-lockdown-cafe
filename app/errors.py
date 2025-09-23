class VaccineError(Exception):
    """Base class for vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} is not vaccinated!")


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str, expiration_date: object) -> None:
        super().__init__(
            f"{name}'s vaccine expired on {expiration_date}"
        )


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} is not wearing a mask!")
