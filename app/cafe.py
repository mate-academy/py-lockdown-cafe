from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("The visitor is not vaccinated!")
        elif visitor.get("vaccine", {}).get("expiration_date") < date.today():
            raise OutdatedVaccineError("The vaccination period has expired!")
        elif visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("The visitor should wear a mask!")
        return f"Welcome to {self.name}"
