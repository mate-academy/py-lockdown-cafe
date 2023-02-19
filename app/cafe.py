from datetime import date
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Make vaccine!")

        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Remake vaccine!")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Wear the mask!")

        return f"Welcome to {self.name}"
