import datetime
from typing import Any

from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str, Any]) -> str:
        vaccine_data = visitor.get("vaccine")

        if not vaccine_data:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = vaccine_data.get("expiration_date")

        if expiration_date is None:
            raise NotVaccinatedError(
                "Vaccine information is incomplete or missing expiration date"
            )

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccination certificate has expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor must wear a mask")

        return f"Welcome to {self.name}"
