import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today_date = datetime.date.today()

        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        if visitor["vaccine"]["expiration_date"] < today_date:
            raise OutdatedVaccineError("Visitor's vaccine is expired")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor doesn't have mask")

        return f"Welcome to {self.name}"
