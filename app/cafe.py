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
            raise NotVaccinatedError("You must be vaccinated!")

        expiration_date = visitor["vaccine"]["expiration_date"]
        today_date = datetime.date.today()
        if expiration_date < today_date:
            raise OutdatedVaccineError("Your vaccination is outdated!")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You must wear a mask!")

        return f"Welcome to {self.name}"
