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
        current_day = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < current_day:
            raise OutdatedVaccineError("The vaccine is expired")
        if visitor["wearing_a_mask"] is not True:
            raise NotWearingMaskError("All must wear masks")

        return f"Welcome to {self.name}"
