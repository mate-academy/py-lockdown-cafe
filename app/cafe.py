import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        if datetime.date.today() > visitor["vaccine"].get("expiration_date"):
            raise OutdatedVaccineError("Visitor has an outdated vaccination")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor is not wearing the mask")
        return f"Welcome to {self.name}"
