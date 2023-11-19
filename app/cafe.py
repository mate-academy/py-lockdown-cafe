from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                f"{visitor.get('name')} has not been vaccinated"
            )

        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError(
                f"{visitor.get('name')}'s vaccine has expired"
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"{visitor.get('name')} must wear a mask"
            )

        return f"Welcome to {self.name}"
