import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> (
            str
            | NotWearingMaskError
            | NotVaccinatedError
            | OutdatedVaccineError
    ):
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(f"{visitor["name"]} is not vaccinated.")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine is outdated.")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor["name"]} has no mask.")

        return f"Welcome to {self.name}"
