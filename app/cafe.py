import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")
        elif (visitor["wearing_a_mask"] is False
              or not visitor.get("wearing_a_mask")):
            raise NotWearingMaskError("NotWearingMaskError")
        return f"Welcome to {self.name}"
