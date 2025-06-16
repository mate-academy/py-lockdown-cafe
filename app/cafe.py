import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(
            self,
            name: int
    ) -> None:
        self.name = name

    def visit_cafe(
            self,
            visitor: dict
    ) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Hasn't vaccine")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is expired")
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Hasn't mask")
        return f"Welcome to {self.name}"
