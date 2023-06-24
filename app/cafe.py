import datetime

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("Visitor isn't vaccinated.")

        expiration_date = visitor.get("vaccine").get("expiration_date")
        if datetime.date.today() > expiration_date:
            raise OutdatedVaccineError("Visitor's vaccinated"
                                       "certificate is expired.")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor should wearing a mask.")

        return f"Welcome to {self.name}"
