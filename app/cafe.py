import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All visitors must have a vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine must not be expired")
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor must wear masks")
        return f"Welcome to {self.name}"
