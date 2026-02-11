import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError,
                        VaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date is None:
            raise VaccineError("Expiration date is missing.")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated.")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor need to wear mask")
        return f"Welcome to {self.name}"
