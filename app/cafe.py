from datetime import date

from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("All friends should be vaccinated")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("")
        else:
            return f"Welcome to {self.name}"
