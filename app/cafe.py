from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError
)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "NotVaccinatedError, Person should be vaccinated!"
            )
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                "OutdatedVaccineError, Person should be vaccinated!"
            )
        if "wearing_a_mask" not in visitor or visitor[
            "wearing_a_mask"
        ] is False:
            raise NotWearingMaskError(
                "NotWearingMaskError, everyone should have a mask"
            )
        return f"Welcome to {self.name}"
