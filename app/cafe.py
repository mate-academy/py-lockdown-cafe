import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(f'{visitor["name"]} is not vaccinated!')
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f'Vaccine is expired for {visitor["name"]}!'
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f'{visitor["name"]} is not wearing a mask!'
            )

        return f"Welcome to {self.name}"
