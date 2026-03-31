from datetime import date
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You need a vaccine to get in!")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Update your vaccine!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Put on your mask!")

        return f"Welcome to {self.name}"
