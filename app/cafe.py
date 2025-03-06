from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You can't enter cafe")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Outdated of your vaccine")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You should buy a mask")

        return f"Welcome to {self.name}"
