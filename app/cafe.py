import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self: "Cafe", name: str) -> None:
        self.name = name

    def visit_cafe(self: "Cafe", visitor: dict) -> str:
        name = visitor.get("name", "Visitor")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{name} is not vaccinated."
            )

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"{name}'s vaccine has expired."
            )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{name} is not wearing a mask."
            )

        return f"Welcome to {self.name}"