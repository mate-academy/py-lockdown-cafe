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
            raise NotVaccinatedError("Visitor doesn't vaccinated!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccination period expired!")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitors have to be on masks!")
        return f"Welcome to {self.name}"
