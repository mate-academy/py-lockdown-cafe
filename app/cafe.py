from app import errors
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise errors.NotVaccinatedError("The visitor should be vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise errors.OutdatedVaccineError("Your vaccine is outdated")

        if not visitor["wearing_a_mask"]:
            raise errors.NotWearingMaskError("The visitor should wear a mask")

        return f"Welcome to {self.name}"
