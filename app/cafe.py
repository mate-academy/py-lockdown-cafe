import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("The vaccine must not be expired")
        if visitor["wearing_a_mask"] is not True:
            raise NotWearingMaskError("All visitors must wear masks")

        return f"Welcome to {self.name}"
