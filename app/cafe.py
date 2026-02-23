import app.errors
import datetime


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not isinstance(vaccine, dict) or "expiration_date" not in vaccine:
            raise app.errors.NotVaccinatedError

        current_day = datetime.date.today()
        expiration_day = vaccine["expiration_date"]

        if current_day > expiration_day:
            raise app.errors.OutdatedVaccineError

        if not visitor.get("wearing_a_mask", False):
            raise app.errors.NotWearingMaskError

        return f"Welcome to {self.name}"
