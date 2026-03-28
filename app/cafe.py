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
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                f"Visitor is not vaccinated "
                f"and cannot enter {self.name}."
            )

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor has an expired vaccine "
                f"(expired on {expiration_date}). "
                f"Access to {self.name} denied."
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"Visitor is not wearing a mask. "
                f"A mask is required to enter {self.name}."
            )

        return f"Welcome to {self.name}"
