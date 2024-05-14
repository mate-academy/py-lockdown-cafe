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
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                "visitor dictionary has no key 'vaccine'"
            )
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "vaccine expiration_date is older than today"
            )
        elif visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("visitor wearing_a_mask is False")
        return f"Welcome to {self.name}"
