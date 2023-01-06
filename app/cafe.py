import datetime
from app.errors import (
    NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        rules_violated = 0
        if "vaccine" not in visitor:
            rules_violated += 1
            raise NotVaccinatedError("The visitor is not vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            rules_violated += 1
            raise OutdatedVaccineError("The visitor's vaccine is expired")
        if not visitor["wearing_a_mask"]:
            rules_violated += 1
            raise NotWearingMaskError("The visitor is not wearing a mask")
        if rules_violated == 0:
            return f"Welcome to {self.name}"
