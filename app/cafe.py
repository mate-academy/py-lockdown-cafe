import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine", None):
            raise NotVaccinatedError("Get a vaccine!")
        if (visitor.get("vaccine").get("expiration_date")
                < datetime.date.today()):
            raise OutdatedVaccineError("Update a vaccine!")
        if not visitor.get("wearing_a_mask", None):
            raise NotWearingMaskError("Get a mask!")
        else:
            return f"Welcome to {self.name}"
