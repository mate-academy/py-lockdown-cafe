from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                f"Visitor {visitor['name']} doesn't have a vaccine!"
            )
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f"Visitor {visitor['name']} has an outdated vaccine!"
            )
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"Visitor {visitor['name']} is not wearing a mask!"
            )
        return f"Welcome to {self.name}"
