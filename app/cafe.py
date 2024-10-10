import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor_vaccine := visitor.get("vaccine"):
            if visitor_vaccine["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Outdated vaccine")
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Not vaccinated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Not wearing mask")
        return f"Welcome to {self.name}"
