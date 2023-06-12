import datetime


from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Error. Visitors have to be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Error. Vaccine is outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Error. Visitors have to be in masks")

        return f"Welcome to {self.name}"
