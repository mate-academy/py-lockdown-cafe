import datetime
from app.errors import (NotWearingMaskError,
                        NotVaccinatedError, OutdatedVaccineError)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Friend should be vaccinated")
        if visitor.get("vaccine"):
            if (visitor.get("vaccine").get("expiration_date")
                    < datetime.date.today()):
                raise OutdatedVaccineError("Your vaccine has expired")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("You should be wearing a mask")
        else:
            return f"Welcome to {self.name}"
