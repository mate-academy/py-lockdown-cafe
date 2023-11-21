import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Everyone should be vaccinated")
        if (datetime.date.today() > visitor.get("vaccine")
                .get("expiration_date")):

            raise OutdatedVaccineError("Vaccination should be valid")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                "Even vaccinated visitors should wear masks")
        return f"Welcome to {self.name}"
