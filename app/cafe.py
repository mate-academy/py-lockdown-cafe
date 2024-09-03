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
            raise NotVaccinatedError(f"{visitor["name"]} should be vaccinated")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor["name"]} "
                                       f"vaccine was expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor["name"]} should buy mask")

        return f"Welcome to {self.name}"
