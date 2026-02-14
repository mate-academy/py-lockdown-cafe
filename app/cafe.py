import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")

        if (
            not isinstance(expiration_date, datetime.date)
            or expiration_date < datetime.date.today()
        ):
            raise OutdatedVaccineError("Vaccine is outdated or invalid")

        if "wearing_a_mask" in visitor and not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
