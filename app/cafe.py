import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine", False):
            raise NotVaccinatedError("All visitors must be vaccinated!!!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine outdated!!!")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitors must wear masks!!!")
        return f"Welcome to {self.name}"
