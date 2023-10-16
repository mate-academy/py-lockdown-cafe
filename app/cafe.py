from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Vaccination certificate missing!")
        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError("Vaccination certificate outdated!")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor isn't wearing a mask!")
        return f"Welcome to {self.name}"
