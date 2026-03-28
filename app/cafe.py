import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Visitor must be vaccinated")

        vaccine_expiration_date = visitor.get("vaccine").get("expiration_date")
        if vaccine_expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        is_visitor_have_mask = visitor.get("wearing_a_mask")
        if not is_visitor_have_mask:
            raise NotWearingMaskError("Visitor must be wearing a mask")

        return f"Welcome to {self.name}"
