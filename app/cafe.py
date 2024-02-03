from app.errors import (NotWearingMaskError,
                        OutdatedVaccineError,
                        NotVaccinatedError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Someone is not vaccinated")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("The vaccine is not suitable")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Someone without a mask")
        return f"Welcome to {self.name}"
