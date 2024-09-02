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
            raise NotVaccinatedError("Visitor does not have a vaccine record.")

        vaccine = visitor.get("vaccine", {})
        expiration_date = vaccine.get("expiration_date")

        if expiration_date is None:
            raise OutdatedVaccineError("Vaccine expiration date is missing.")
        elif expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine has expired.")

        if ("wearing_a_mask" not in visitor
                or visitor["wearing_a_mask"] is False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
