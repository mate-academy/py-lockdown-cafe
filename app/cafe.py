import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor must be vaccinated!")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Vaccination must "
                                       "be is not expired!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitors must wear masks!")
        return f"Welcome to {self.name}"

    def __str__(self) -> str:
        return self.name
