import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "You need to be vaccinated to enter the cafe.")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "Your vaccine is outdated. Please update your vaccination.")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "You must wear a mask to enter the cafe.")

        return f"Welcome to {self.name}"
