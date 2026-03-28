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
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError(
                "Entry is not allowed without vaccination."
            )
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "Your vaccine has expired. Vaccinate again."
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "Entry is not allowed without a mask. Wear a mask!"
            )
        return f"Welcome to {self.name}"
