import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor isn't vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("the vaccine for visitors is outdated")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("visitors without masks")

        return f"Welcome to {self.name}"
