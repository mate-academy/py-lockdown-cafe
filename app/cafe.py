from datetime import date

from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str | NotVaccinatedError | NotWearingMaskError:
        if visitor.get("vaccine") is None:
            raise NotVaccinatedError("You aren't vaccinated!")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Your vaccine has expired!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You aren't wearing a mask!")
        return f"Welcome to {self.name}"
