import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str | NotVaccinatedError | OutdatedVaccineError | NotWearingMaskError:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("Person is not vaccinated!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vacccine is outdated!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Person must wear a mask")
        return f"Welcome to {self.name}"
