import datetime
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        wearing_a_mask = visitor.get("wearing_a_mask", False)

        if vaccine is None:
            raise NotVaccinatedError("Visitor is not vaccinated")
        elif vaccine.get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")
        elif not wearing_a_mask:
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
