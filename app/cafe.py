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
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{self.name} is not vaccinated"
            )

        if date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                f'{visitor["name"]}\'s vaccine is outdated'
            )

        if (
                "wearing_a_mask" not in visitor
                or visitor["wearing_a_mask"] is False
        ):
            raise NotWearingMaskError(
                f'{visitor["name"]} is not a wearing mask'
            )

        return f"Welcome to {self.name}"
