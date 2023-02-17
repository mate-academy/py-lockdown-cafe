from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor['name']} has no vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("vaccine has expired")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError(
                f"{visitor['name']} not wearing the mask"
            )
        return f"Welcome to {self.name}"
