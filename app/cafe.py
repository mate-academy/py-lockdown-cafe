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
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                f"Visitor {visitor["name"]} does not have vaccine."
            )

        expiration_date = visitor["vaccine"]["expiration_date"]

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor["name"]}'s vaccine has expired."
            )

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"Visitor {visitor["name"]} does not wear a mask."
            )

        return f"Welcome to {self.name}"
