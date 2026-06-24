from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        visitor_name = visitor.get("name")
        visitor_vaccine = visitor.get("vaccine")

        if not visitor_vaccine:
            raise NotVaccinatedError(visitor_name)

        exp_date = visitor_vaccine.get("expiration_date")
        if isinstance(exp_date, str):
            exp_date = date.fromisoformat(exp_date)

        if exp_date < date.today():
            raise OutdatedVaccineError(visitor_name)

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(visitor_name)

        return f"Welcome to {self.name}"
