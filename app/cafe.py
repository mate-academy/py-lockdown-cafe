from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor.get("name", "Unknown")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"Visitor {name} is not vaccinated.")

        vaccine = visitor["vaccine"]
        expiration_date = vaccine["expiration_date"]
        today = date.today()

        if expiration_date < today:
            raise OutdatedVaccineError(
                f"Visitor {name} has an outdated vaccine."
            )

        wearing_mask = visitor.get("wearing_a_mask", False)

        if not wearing_mask:
            raise NotWearingMaskError(f"Visitor {name} is not wearing a mask.")

        return f"Welcome to {self.name}"
