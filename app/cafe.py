import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("You have to vaccine yourself")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("You have to vaccine again")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("You have to buy a mask")
        return f"Welcome to {self.name}"
