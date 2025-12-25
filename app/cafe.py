import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Where vaccinate? You "
                                     "believe in a flat Earth?")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Dude, check your date of vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("No mask, no food, loser.")
        return f"Welcome to {self.name}"
