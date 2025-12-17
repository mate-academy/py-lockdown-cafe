from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> any:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
