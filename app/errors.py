from datetime import datetime


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        super().__init__("Not vaccinated")


class OutdatedVaccineError(VaccineError):
    def __init__(
            self,
            expiration_date: datetime
    ) -> None:
        super().__init__(
            f"Vaccine expired on {expiration_date}"
        )


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        super().__init__("Not wearing a mask")
