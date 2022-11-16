from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, \
    NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            visitor["vaccine"]
        except KeyError:
            raise NotVaccinatedError("All friends should be vaccinated")
        try:
            date = visitor["vaccine"].get("expiration_date")
            assert date >= datetime.date.today()
        except AssertionError:
            raise OutdatedVaccineError("OutdatedVaccineError")
        if visitor["wearing_a_mask"] is not True:
            raise NotWearingMaskError("NotWearingMaskError")
        else:
            return f"Welcome to {self.name}"
