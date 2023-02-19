import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("NotVaccinatedError in line 13")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError in line 15")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("NotWearingMaskError in line 17")
        return f"Welcome to {self.name}"
