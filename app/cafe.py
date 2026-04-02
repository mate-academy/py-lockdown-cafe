import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if 'vaccine' not in visitor:
            raise NotVaccinatedError(
                f"Visitor {visitor['name']} is not vaccinated.")
        today = datetime.date.today()
        vaccination_day = visitor['vaccine']['expiration_date']
        if vaccination_day < today:
            raise OutdatedVaccineError(
                f"Vaccine visitor {visitor['name']} is off.")
        if visitor.get("wearing_a_mask") is not True:
            raise NotWearingMaskError(
                f"Visitor {visitor['name']} must wear a mask")
        return f"Welcome to {self.name}"
