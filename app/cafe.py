import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        current_visitor = visitor.get("vaccine", False)
        expiry = current_visitor.get(
            "expiration_date", False
        ) if current_visitor else False

        if not current_visitor:
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated")
        if current_visitor and expiry:
            today = datetime.date.today()
            if today > expiry:
                raise OutdatedVaccineError(
                    f"Vaccine of {visitor['name']} is outdated"
                )
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor['name']} is not wearing a mask"
            )

        return f"Welcome to {self.name}"
