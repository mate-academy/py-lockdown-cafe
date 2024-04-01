import datetime
from app.errors import (NotWearingMaskError,
                        OutdatedVaccineError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is expired")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor must be wearing a mask")
        return f"Welcome to {self.name}"
