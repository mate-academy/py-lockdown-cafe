from datetime import date


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
            raise NotVaccinatedError("The visitor does not have a vaccine")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("The visitor has a outdated vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The visitor is not wearing a mask")
        return f"Welcome to {self.name}"
