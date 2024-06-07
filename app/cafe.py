import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated.")
        elif today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Visitor has expired vaccine.")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor must wear mask.")
        else:
            return f"Welcome to {self.name}"
