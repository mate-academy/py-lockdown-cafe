from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" in visitor:
            exp_date = visitor.get("vaccine").get("expiration_date")
            if exp_date < datetime.date.today():
                raise OutdatedVaccineError("Your vaccine is expired!")
        else:
            raise NotVaccinatedError("You should be vaccinated!")

        visitor_has_mask = visitor.get("wearing_a_mask", False)
        if visitor_has_mask:
            return f"Welcome to {self.name}"
        else:
            raise NotWearingMaskError("You should wear a mask!")
