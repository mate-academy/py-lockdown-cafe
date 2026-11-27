import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> str | None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        today = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated")
        elif visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("You fell for the scam")
        elif (
            "wearing_a_mask" not in visitor
            or visitor["wearing_a_mask"] is False
        ):
            raise NotWearingMaskError("Good job, freedom fighter!")
        else:
            return f"Welcome to {self.name}"
