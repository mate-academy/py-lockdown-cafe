from datetime import date
from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError("Not vaccine")

        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise errors.OutdatedVaccineError("Your vaccine outdated ")

        if not visitor.get("wearing_a_mask"):
            raise errors.NotWearingMaskError("You didn't have a mask")

        return f"Welcome to {self.name}"
