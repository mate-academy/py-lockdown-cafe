import datetime

from app.errors import (NotVaccinatedError,
                        NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if not visitor.get("vaccine"):

            raise NotVaccinatedError("You must be vaccinated!")

        elif (visitor["vaccine"].get("expiration_date")
              and visitor["vaccine"]["expiration_date"]
              < datetime.date.today()):

            raise OutdatedVaccineError("Your vaccine has outdated")

        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Please buy mask!")

        return f"Welcome to {self.name}"
