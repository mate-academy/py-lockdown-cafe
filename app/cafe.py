import datetime
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            visitor_name = visitor.get("name", "Visitor")
            raise NotVaccinatedError(
                f"{visitor_name} is not vaccinated"
            )

        vaccine_info = visitor["vaccine"]
        if "expiration_date" in vaccine_info:
            if vaccine_info["expiration_date"] < datetime.date.today():
                visitor_name = visitor.get("name", "Visitor")
                raise OutdatedVaccineError(
                    f"{visitor_name}'s vaccine is outdated"
                )

        if not visitor.get("wearing_a_mask", False):
            visitor_name = visitor.get("name", "Visitor")
            raise NotWearingMaskError(
                f"{visitor_name} is not wearing a mask"
            )

        return f"Welcome to {self.name}"
