import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are not vaccinated!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine has outdated!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Sorry, you are not allowed "
                                      "to the cafe due to absence "
                                      "of the vaccine!")
        return f"Welcome to {self.name}"
