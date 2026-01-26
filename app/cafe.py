import datetime

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        is_vaccined = visitor.get("vaccine", False)
        is_wearing_a_mask = visitor.get("wearing_a_mask", False)

        if not is_vaccined:
            raise NotVaccinatedError

        if is_vaccined["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError

        if not is_wearing_a_mask:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
