import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        elif visitor["vaccine"].get("expiration_date",
                                    datetime.date.min) < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdate")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Please, buy the mask")
        return f"Welcome to {self.name}"
