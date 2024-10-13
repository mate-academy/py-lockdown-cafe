import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        visitor_date = visitor["vaccine"]["expiration_date"]
        if visitor_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
