import datetime

from app.errors import (
    OutdatedVaccineError,
    NotVaccinatedError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        person = visitor["name"]

        if not visitor.get("vaccine"):
            raise NotVaccinatedError(person)

        if visitor.get("vaccine", {}).get(
                "expiration_date"
        ) < datetime.date.today():
            raise OutdatedVaccineError(person)

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(person)

        return f"Welcome to {self.name}"
