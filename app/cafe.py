import datetime
from app.errors import NotWearingMaskError
from app.errors import (NotVaccinatedError, OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> str:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor is not vaccinated")

        expiration_date = visitor["vaccine"]["expiration_date"]
        today = datetime.date.today()

        if expiration_date < today:
            raise OutdatedVaccineError("Vaccine is expired")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor should wear a mask")

        return f"Welcome to {self.name}"
