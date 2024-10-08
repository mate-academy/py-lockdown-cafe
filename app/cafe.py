import datetime

from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("All friends should be vaccinated")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine is out of date")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You should wear mask")
        return f"Welcome to {self.name}"
