import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        expiration_date = visitor.get("vaccine", {}).get("expiration_date")
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor doesn`t vaccinated")
        elif expiration_date < today:
            raise OutdatedVaccineError("Vaccine expired")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
