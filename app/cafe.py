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
            raise NotVaccinatedError("You are not vaccinated"
                                     " - vaccination is important!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your vaccine has expired"
                                       " - you need to revaccinate!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The mask "
                                      "reduces the risk of infection"
                                      " - with a mask calmer!")
        return f"Welcome to {self.name}"
