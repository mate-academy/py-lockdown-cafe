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
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(
                f"{visitor['name']} is not vaccinated!"
            )
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']} has an outdated vaccine!"
            )
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError(
                f"{visitor['name']} doesn't have a mask!"
            )

        return f"Welcome to {self.name}"
