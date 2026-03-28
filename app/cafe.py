import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" in visitor:
            vaccine = visitor.get("vaccine")
            today = datetime.date.today()
            if vaccine.get("expiration_date") >= today:
                if visitor.get("wearing_a_mask"):
                    return f"Welcome to {self.name}"
                raise NotWearingMaskError("Visitor is not wearing mask!")
            raise OutdatedVaccineError("Visitor's vaccine is expired!")
        raise NotVaccinatedError("Visitor not Vaccinated!")
