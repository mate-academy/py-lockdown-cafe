from datetime import date
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        today = date.today()
        visitor_vaccine = visitor.get("vaccine")
        if visitor_vaccine is None:
            raise NotVaccinatedError("Visitor is not vaccinated")
        vaccine_expiration_date = visitor_vaccine.get("expiration_date")
        if (vaccine_expiration_date is not None
                and vaccine_expiration_date < today):
            raise OutdatedVaccineError("Visitor vaccines expired")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Visitor is not wearing mask")

        return f"Welcome to {self.name}"
