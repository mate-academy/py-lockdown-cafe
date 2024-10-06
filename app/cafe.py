from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f'{visitor["name"]} is not vaccinated!'
            )

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < date.today():
            raise OutdatedVaccineError(
                f'{visitor["name"]}\'s vaccine is outdated!'
            )

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f'{visitor["name"]} is not wearing a mask!'
            )

        return f"Welcome to {self.name}"
