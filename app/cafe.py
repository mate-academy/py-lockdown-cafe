import datetime

from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("NotVaccinatedError")

        expiration_date = visitor["vaccine"].get("expiration_date")

        if expiration_date is None or expiration_date < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
