from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Not Vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]

        if expiration_date < today:
            raise OutdatedVaccineError("Vaccined is not valid")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You have not a mask")
        else:
            return f"Welcome to {self.name}"
