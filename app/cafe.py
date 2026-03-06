import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(
        self,
        name: str
    ) -> None:
        self.name = name

    def visit_cafe(
        self,
        visitor: dict
    ) -> str:
        vaccine = visitor.get("vaccine")

        if vaccine is None:
            raise NotVaccinatedError(
                f'{visitor["name"]} is not vaccinated'
            )

        if vaccine["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f'{visitor["name"]} has an outdated vaccine'
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f'{visitor["name"]} is not wearing a mask'
            )

        return f"Welcome to {self.name}"
