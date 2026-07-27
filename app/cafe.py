import datetime

import app.errors as errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise errors.NotVaccinatedError("Visitor has not been vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise errors.OutdatedVaccineError("Vaccine has expired")
        elif visitor["wearing_a_mask"] is False:
            raise errors.NotWearingMaskError("Visitor is not wearing a mask")
        return f"Welcome to {self.name}"
