import datetime
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError("User is not vaccinated")
        expiration_date = vaccine.get("expiration_date")
        today_date = datetime.date.today()
        if (
            isinstance(expiration_date, datetime.date)
            and expiration_date < today_date
        ):
            raise OutdatedVaccineError("Outdated vaccine date")
        wearing_a_mask = visitor.get("wearing_a_mask")
        if not wearing_a_mask:
            raise NotWearingMaskError("User is not wearing mask")
        return f"Welcome to {self.name}"
