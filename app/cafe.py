import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError:"
                                     " the visitor is not vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError:"
                                       " the visitor's vaccine is out of date")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("NotWearingMaskError: "
                                      " visitor without a mask")
        return f"Welcome to {self.name}"
