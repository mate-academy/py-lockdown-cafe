import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All visitor must be vaccine")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine time is over")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("All visitor must wear mask")
        else:
            return f"Welcome to {self.name}"
