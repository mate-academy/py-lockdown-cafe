from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("All visitors "
                                     "must be vaccinated! Please do it")
        try:
            date = visitor.get("vaccine").get("expiration_date")
            assert date >= datetime.date.today()
        except (AssertionError, AttributeError):
            raise OutdatedVaccineError("Vaccine expired! Go home , dude ! ")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Buy a mask, don't infect others !")
        return f"Welcome to {self.name}"
