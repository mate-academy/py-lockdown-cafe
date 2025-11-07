import datetime

from app.errors import (
    NotWearingMaskError,
    OutdatedVaccineError,
    NotVaccinatedError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated")

        if visitor.get("vaccine").get("expiration_date") < \
                datetime.date.today():
            raise OutdatedVaccineError("Vaccination certificate has expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor must wear a mask")

        return f"Welcome to {self.name}"
