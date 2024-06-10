from datetime import date
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")

        if ("expiration_date" not in visitor["vaccine"]
                or visitor["vaccine"]["expiration_date"] < date.today()):
            raise OutdatedVaccineError("OutdatedVaccineError")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
