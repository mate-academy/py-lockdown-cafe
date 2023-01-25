import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Person should be vaccinated.")
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("The person vaccine has expired.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Person doesn't wear a mask.")
        return f"Welcome to {self.name}"
