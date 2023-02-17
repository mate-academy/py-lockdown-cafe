from datetime import date

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Visitor isn`t vaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Visitor have overdue vaccination")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor don`t wear mask")
        return f"Welcome to {self.name}"
