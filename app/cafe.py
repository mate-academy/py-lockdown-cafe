from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        elif visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"
