import datetime

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name
        self.date = datetime.date.today()

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(" ")
        elif visitor["vaccine"]["expiration_date"] < self.date:
            raise OutdatedVaccineError(" ")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(" ")
        else:
            return f"Welcome to {self.name}"
