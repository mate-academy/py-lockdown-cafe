import datetime
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
            raise NotVaccinatedError(
                f"Vaccine is required to visit {self.name}"
            )

        if (visitor.get("vaccine").get("expiration_date")
                < datetime.date.today()):

            raise OutdatedVaccineError(
                f"Date must be not less than today to visit {self.name}"
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"Mask is required to visit {self.name}"
            )

        return f"Welcome to {self.name}"
