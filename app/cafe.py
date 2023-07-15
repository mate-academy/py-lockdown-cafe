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
            raise NotVaccinatedError("Visitors must be vaccinated")
        else:
            if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
                raise OutdatedVaccineError("Vaccine is outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitors must wear a mask")
        return f"Welcome to {self.name}"
