import datetime
from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError,
                        NotVaccinatedError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Vaccine is not")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(visitor["vaccine"]["expiration_date"])
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Wearing mask")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Wearing mask")
        return f"Welcome to {self.name}"
