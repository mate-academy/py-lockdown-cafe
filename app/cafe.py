from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        current_date = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor isn't vaccinated.")
        if visitor["vaccine"]["expiration_date"] < current_date:
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask.")
        return f"Welcome to {self.name}"
