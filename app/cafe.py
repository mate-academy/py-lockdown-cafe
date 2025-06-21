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
        vaccine = visitor.get("vaccine")

        if not vaccine:
            raise NotVaccinatedError("Visitor must be vaccinated")

        current_date = datetime.date.today()
        vaccine_date = vaccine.get("expiration_date")

        if vaccine_date < current_date:
            raise OutdatedVaccineError("The vaccine should not be outdated")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Wearing a mask is mandatory")

        return f"Welcome to {self.name}"
