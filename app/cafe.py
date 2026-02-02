import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitors vaccine is outdated!")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Every visitor have to wear mask!")
        return f"Welcome to {self.name}"
