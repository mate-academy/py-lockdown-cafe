import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You can not enter our cafe"
                                     " if you are not vaccinated, sorry.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Your vaccination is out of date. "
                                       "You can not enter our cafe"
                                       " if you are not vaccinated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Everyone should wear the mask"
                                      " in our cafe")
        else:
            return f"Welcome to {self.name}"
