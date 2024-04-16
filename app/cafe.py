import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"Vaccine expired on {expiration_date}")

        if (visitor.get("wearing_a_mask") is False
                or not visitor.get("wearing_a_mask")):
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
