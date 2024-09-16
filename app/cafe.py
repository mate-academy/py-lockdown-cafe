from datetime import date
from app.errors import (
    VaccineError,
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if "vaccine" not in visitor:
                raise NotVaccinatedError("NotVaccinatedError")
            if visitor["vaccine"]["expiration_date"] < date.today():
                raise OutdatedVaccineError("OutdatedVaccineError")
            if visitor["wearing_a_mask"] is False:
                raise NotWearingMaskError("NotWearingMaskError")
        except VaccineError:
            raise
        except NotWearingMaskError:
            raise
        else:
            return f"Welcome to {self.name}"
