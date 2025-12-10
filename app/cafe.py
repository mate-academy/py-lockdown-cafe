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
        today = datetime.date.today()
        if (
                "vaccine" not in visitor.keys()
                or not visitor["vaccine"].get("expiration_date")
        ):
            raise NotVaccinatedError("You don't have a vaccine")
        elif visitor["vaccine"].get("expiration_date", today) < today:
            raise OutdatedVaccineError("Your vaccine is expired")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("No entry without a mask")
        return f"Welcome to {self.name}"
