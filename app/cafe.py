import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError("You should be vaccinated")
        if today > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("You should be vaccinated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You should put on a mask")
        return f"Welcome to {self.name}"
