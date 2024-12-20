import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f'{visitor["name"]} vaccine is expired.')

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                "All friends should be vaccinated")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f'{visitor["name"]} must wearing mask.')

        return f"Welcome to {self.name}"
