from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)
import datetime

today = datetime.date.today()


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("Vaccine expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
