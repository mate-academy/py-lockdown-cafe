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

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        if visitor["vaccine"]:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Vaccine be expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor doesn't wear a mask")

        return f"Welcome to {self.name}"
