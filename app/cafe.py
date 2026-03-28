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
                f'{visitor.get("name")} is not vaccinated!'
            )
        if (visitor.get("vaccine").get("expiration_date")
                < datetime.date.today()):
            raise OutdatedVaccineError(
                f'{visitor.get("name")}s vaccine is outdated!'
            )
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError(
                f'{visitor.get("name")} is not wearing a mask!'
            )
        return f"Welcome to {self.name}"
