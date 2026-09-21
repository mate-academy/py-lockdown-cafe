from app.errors import (NotVaccinatedError, NotWearingMaskError,
                        OutdatedVaccineError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]
        today = datetime.date.today()
        if expiration_date < today:
            raise OutdatedVaccineError("Vaccine is expired")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing mask")

        return f"Welcome to {self.name}"
