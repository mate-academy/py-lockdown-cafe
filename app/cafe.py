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
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine_exp_date = visitor.get("vaccine", {}).get("expiration_date")

        today = datetime.date.today()

        if vaccine_exp_date < today:
            raise OutdatedVaccineError("Vaccine date is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor must wear a mask")
        return f"Welcome to {self.name}"
