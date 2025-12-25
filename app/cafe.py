import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You should be vaccinated")

        today_date = datetime.date.today()
        if visitor["vaccine"]["expiration_date"] < today_date:
            raise OutdatedVaccineError("Your vaccine is expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You should wear a mask")

        return f"Welcome to {self.name}"
