import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("No vaccine - no burgers")

        today = datetime.date.today()

        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("A new dose of vaccine is needed")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("WHERE IS THE MASK????")

        return f"Welcome to {self.name}"
