import datetime

from app.errors import (NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today_date = datetime.date.today()

        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError("Person is not vaccinated")

        expiration_date = vaccine.get("expiration_date")
        if not expiration_date or expiration_date < today_date:
            raise OutdatedVaccineError("Vaccine has expired")

        wearing_a_mask = visitor.get("wearing_a_mask", False)
        if not wearing_a_mask:
            raise NotWearingMaskError("Person is not wearing a mask")

        return f"Welcome to {self.name}"