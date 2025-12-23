import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are not vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]
        now_day = datetime.date.today()

        if expiration_date < now_day:
            raise OutdatedVaccineError("Your vaccine out of date")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You don't have a mask")

        return f"Welcome to {self.name}"
