from datetime import date
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Sorry, access denied. "
                                     "The visitor should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Sorry, we can't let you in."
                                       " Your vaccination is outdated")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Please wear your mask,"
                                      " then you will able to visit the cafe")
        return f"Welcome to {self.name}"
