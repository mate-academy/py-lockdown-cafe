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
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Person should be vaccinated!")

        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("Person vaccination key is outdated")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Person don`t have wearing mask")

        return f"Welcome to {self.name}"
