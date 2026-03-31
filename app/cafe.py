import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("All friends should be vaccinated")
        relevant_date = visitor["vaccine"]["expiration_date"]
        if relevant_date < datetime.date.today():
            raise OutdatedVaccineError("Your vaccination is old")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Friend should buy mask")
        return f"Welcome to {self.name}"
