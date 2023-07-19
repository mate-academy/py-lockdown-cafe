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
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor has not vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]
        today_date = datetime.date.today()

        if expiration_date < today_date:
            raise OutdatedVaccineError("Your date of vaccination is not valid")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Please wear your mask on the face")

        return f"Welcome to {self.name}"
