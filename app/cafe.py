from datetime import date
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name
        self.count = 0

    def visit_cafe(self, visitor: dict) -> str:
        today = date.today()
        if not visitor.get("vaccine"):
            raise NotVaccinatedError
        if today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError
        if not visitor["wearing_a_mask"]:
            self.count += 1
            raise NotWearingMaskError(f"Friends should buy {self.count} masks")
        return f"Welcome to {self.name}"
