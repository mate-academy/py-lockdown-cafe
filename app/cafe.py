import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        if not vaccine:
            raise NotVaccinatedError(
                f"Visitor '{visitor.get("name", "Unknown")}' is not "
                "vaccinated and cannot enter the cafe."
            )

        expiration_date = vaccine.get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"Visitor '{visitor.get("name", "Unknown")}' has an "
                f"expired vaccine certificate (expired on {expiration_date})."
            )

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                f"Visitor '{visitor.get("name", "Unknown")}' is not wearing "
                "a mask and cannot enter the cafe."
            )

        return f"Welcome to {self.name}"
