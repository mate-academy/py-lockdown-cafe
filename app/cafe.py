import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("The visitor must have the vaccine.")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine expired.")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("The visitor must have a mask.")
        else:
            return f"Welcome to {self.name}"
