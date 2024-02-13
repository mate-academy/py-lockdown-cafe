from app.errors import (OutdatedVaccineError,
                        NotWearingMaskError, NotVaccinatedError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine"):
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("The vaccine expired")
            if visitor["wearing_a_mask"] is False:
                raise NotWearingMaskError("You must wear a mask")
        else:
            raise NotVaccinatedError("You must be vaccinated")
        return f"Welcome to {self.name}"
