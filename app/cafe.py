from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        count = 0
        if "vaccine" not in visitor:
            count += 1
            raise NotVaccinatedError("The client does not have a vaccine")

        if visitor["vaccine"]["expiration_date"] < date.today():
            count += 1
            raise OutdatedVaccineError("The client's vaccine is expired")

        if visitor["wearing_a_mask"] is False:
            count += 1
            raise NotWearingMaskError("The client does not have a mask")

        if count == 0:
            return f"Welcome to {self.name}"
