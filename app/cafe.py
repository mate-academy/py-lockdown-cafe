import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccinated = visitor.get("vaccine", None)
        mask = visitor.get("wearing_a_mask", None)
        if vaccinated:
            vaccine_expire_date = visitor.get("vaccine").get("expiration_date")

        if not vaccinated:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        elif vaccine_expire_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine has expired.")
        elif not mask:
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
