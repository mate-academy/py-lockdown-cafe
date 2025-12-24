import datetime
from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("You must be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Yours Vaccine out of dated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You must buy mask")
        return f"Welcome to {self.name}"
