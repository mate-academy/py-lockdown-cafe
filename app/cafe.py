import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor.get("vaccine").get("expiration_date")
        acurate_data = datetime.date.today()

        if acurate_data > expiration_date:
            raise OutdatedVaccineError("Visitor's vaccine has expired")

        if visitor.get("wearing_a_mask") is True:
            return f"Welcome to {self.name}"
        else:
            raise NotWearingMaskError("Visitor is not wearing a mask")
