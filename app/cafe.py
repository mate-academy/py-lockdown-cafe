from datetime import date

from app.errors import (
    NotVaccinatedError, NotWearingMaskError, OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends must be vaccinated.")

        if visitor.get("vaccine").get("expiration_date") < date.today():
            raise OutdatedVaccineError(
                "There are friends with expired vaccines."
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("All friends must wear masks.")

        return f"Welcome to {self.name}"
