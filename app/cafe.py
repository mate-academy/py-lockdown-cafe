import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: int) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> any:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError("NotVaccinatedError")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(OutdatedVaccineError)

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(NotWearingMaskError)

        return f"Welcome to {self.name}"
