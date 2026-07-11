import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, object]) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor need vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's "
                                       "vaccine has "
                                       "expired and is no "
                                       "longer valid.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor "
                                      "must wear a mask to enter the cafe.")
        return f"Welcome to {self.name}"
