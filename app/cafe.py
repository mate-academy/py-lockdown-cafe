import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError("you need to get vaccinated")

        if visitor.get("vaccine").get("expiration_date") < today:
            raise OutdatedVaccineError("your vaccine is outdated")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("you forgot to put on your mask")

        return f"Welcome to {self.name}"
