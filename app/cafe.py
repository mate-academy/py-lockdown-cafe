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
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated.")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError(
                f"{visitor['name']} has an expired vaccination"
            )
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                f"{visitor['name']} didn't wear the mask"
            )

        return f"Welcome to {self.name}"
