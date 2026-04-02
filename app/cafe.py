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
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError

        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError

        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError

        else:
            return f"Welcome to {self.name}"
