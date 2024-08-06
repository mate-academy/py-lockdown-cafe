import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        all_rule_done = True
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated.")
            all_rule_done = False
        if (visitor.get("vaccine").get("expiration_date")
                < datetime.date.today()):
            raise OutdatedVaccineError("Visitor's vaccine is expired.")
            all_rule_done = False
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask.")
            all_rule_done = False
        if all_rule_done:
            return (f"Welcome to {self.name}")
