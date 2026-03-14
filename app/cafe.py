import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        ex_date = visitor["vaccine"]["expiration_date"]
        if ex_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor must wear a mask")
        return f"Welcome to {self.name}"
