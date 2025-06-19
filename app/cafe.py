from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("You are not vaccinated")
        if (visitor["vaccine"]["expiration_date"]
                < datetime.date.today()):
            raise OutdatedVaccineError("Your vaccine is outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Wear mask pls")
        return f"Welcome to {self.name}"
