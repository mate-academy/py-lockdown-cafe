import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("The visitor is not vaccinated!")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine is outdated!")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Not wearing mask! Must have one!")
        return f"Welcome to {self.name}"
