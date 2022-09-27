from datetime import date
from app.errors import NotVaccinatedError, NotWearingMaskError, \
    OutdatedVaccineError


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("All visitors must be vaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Vaccine must be valid on the "
                                       "day of visit")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wear a mask")

        return f"Welcome to {self.name}"
