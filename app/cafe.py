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

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Customer should be vaccinated")

        today_date = datetime.date.today()
        if today_date > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("The vaccine is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("The visitor is not wearing a mask")

        return f"Welcome to {self.name}"
