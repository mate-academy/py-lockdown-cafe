from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
    VaccineError,
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | VaccineError:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError
        elif datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError
        elif (
            "wearing_a_mask" not in visitor.keys()
            or not visitor["wearing_a_mask"]
        ):
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
