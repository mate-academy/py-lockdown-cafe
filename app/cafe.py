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
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        today = datetime.date.today()
        expiration_date = visitor["vaccine"]["expiration_date"]

        if expiration_date < today:
            raise OutdatedVaccineError("Visitor's vaccine has expired")

        if ("wearing_a_mask" not in visitor
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError("Visitor is not wearing mask")

        return f"Welcome to {self.name}"
