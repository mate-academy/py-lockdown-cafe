import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']}'s vaccine has expired"
            )
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor['name']} is without mask!")
        return f"Welcome to {self.name}"
