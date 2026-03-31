import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine_info = visitor.get("vaccine")
        if not vaccine_info:
            raise NotVaccinatedError("Visitor is not vaccinated!")
        if vaccine_info["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine has expired!")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Visitor is not wearing a mask!")

        return f"Welcome to {self.name}"
