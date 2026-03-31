import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor should be vaccinated")
        if today > visitor["vaccine"].get("expiration_date"):
            raise OutdatedVaccineError("Visitor should be vaccinated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor should buy mask")
        else:
            return f"Welcome to {self.name}"
