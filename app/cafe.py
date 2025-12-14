import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor does not"
                                     " have 'vaccine'")

        if (visitor.get("vaccine").get("expiration_date")
                < datetime.date.today()):
            raise OutdatedVaccineError("Vaccine is too old")

        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Visitor doesn't have mask")

        return f"Welcome to {self.name}"
