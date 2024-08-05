import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        today = datetime.date.today()

        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Visitors must be vaccinated!")

        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError(
                "The vaccine is outdated! Visitor need to renew vaccination!"
            )

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor need to buy mask!")

        return f"Welcome to {self.name}"
