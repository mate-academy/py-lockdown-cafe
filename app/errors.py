import datetime


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, visitor_name: str) -> None:
        super().__init__(f"{visitor_name} is not vaccinated")


class OutdatedVaccineError(VaccineError):
    def __init__(
            self,
            visitor_name: str,
            expiration_date: datetime.date) -> None:
        message = (
            f"{visitor_name} has an outdated vaccine "
            f"(expired on {expiration_date})"
        )
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, visitor_name: str) -> None:
        super().__init__(f"{visitor_name} is not wearing a mask")
