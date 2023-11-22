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
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"The {self.name} visitor "
                f"{visitor['name']} doesn't have a vaccine!"
            )
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"The {visitor['name']}'s vaccine has expired!"
            )
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                f"The visitor {visitor['name']} doesn't wear a mask!"
            )
        return f"Welcome to {self.name}"
