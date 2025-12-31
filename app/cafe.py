import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # if "vaccine" not in visitor or not visitor["vaccine"]:
        if visitor.get("vaccine", 0) == 0:
            raise NotVaccinatedError("Visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The Vaccine is outdated")
        if visitor["wearing_a_mask"] is not True:
            raise NotWearingMaskError("The Wearing Mask is missing")

        return f"Welcome to {self.name}"
