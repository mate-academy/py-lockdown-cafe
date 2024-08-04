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

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitors must be vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError(
                "The vaccine is outdated! Visitor need to renew vaccination!"
            )
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor need to buy mask!")
        else:
            return f"Welcome to {self.name}"
