import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not Vaccinated")
        if not (visitor["vaccine"]["expiration_date"]
                >= datetime.date.today()):
            raise OutdatedVaccineError("Vaccine is outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor has no mask")

        return f"Welcome to {self.name}"
