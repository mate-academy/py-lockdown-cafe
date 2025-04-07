import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = datetime.date.today()
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You need vaccine to enter this cafe!")
        elif visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError("Your vaccine is expired!")
        elif "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You need to wear mask"
                                      " to enter this cafe!")
        else:
            return f"Welcome to {self.name}"
