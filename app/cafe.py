import datetime

from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor isn't vaccinated.")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccination is expired.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor doesn't have mask.")
        return f"Welcome to {self.name}"
